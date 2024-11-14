import json

from typing import Any, Iterator, Tuple

from bible import BibleRef, BibleSec, evangelists


class BoxRef:
    """Represents a box reference in a translation"""

    def __init__(self, part_idx: int, section_idx_loc: int, section_id: str, e: int, idx: int):
        self.part_idx = part_idx
        self.section_idx_loc = section_idx_loc
        self.section_id = section_id
        self.e = e
        self.idx = idx

    def __repr__(self) -> str:
        return f'({self.section_id};{evangelists[self.e]};{self.idx})'


class Box:

    def __init__(self, loaded_json, e):
        self.json: json = loaded_json
        self.e = e

    def __repr__(self) -> str:
        return str(self.json)

    def is_body(self) -> bool:
        return self.json['leading']

    def iterate(self) -> Iterator[Tuple[BibleRef, str]]:
        for v in self.json['content']:
            yield self._get_ref(v), v['text']

    def length(self) -> int:
        ret = len(self.json['content'])
        assert 0 < ret, f'Box length should be positive. json={self.json}'
        return ret

    def get_sec(self) -> BibleSec:
        length = self.length()
        start = self._get_ref(self.json['content'][0])
        end = self._get_ref(self.json['content'][length - 1]).next()
        return BibleSec(start, end)

    def get_closed_str(self):
        length = self.length()
        start = self._get_ref(self.json['content'][0])
        end = self._get_ref(self.json['content'][length - 1])
        ret = str(start)
        if start == end:
            return ret
        ret = ret + f'-'
        if start.e != end.e:
            return ret + str(end)
        s = {1: 'a', 2: 'b'}.get(end.x, '')
        if start.chapter != end.chapter:
            return ret + str(end.chapter) + ',' + str(end.verse) + s
        return ret + str(end.verse) + s

    def _get_ref(self, content_element) -> BibleRef:
        verse_str = content_element['verse']
        verse, x = BibleRef.split_verse(verse_str)
        return BibleRef(self.e, int(content_element['chapter']), verse, x)


class Translation:
    """Represents a bible translation"""

    def __init__(self, loaded_json):
        self.json: json = loaded_json
        self.part_titles: list[str] = []
        self.section_titles: dict[str, str] = {}
        self.ref_to_text: dict[BibleRef, str] = {}
        self.body_ref_to_box_ref: dict[BibleRef, BoxRef] = {}
        self.body_text_partition: list[BibleSec] = []

        for part, part_idx in self.iterate_on_parts():
            self.part_titles.append(part['part_title'])
        self._init_section_titles()
        self._init_ref_to_text()
        self._init_body_ref_to_box_ref()
        self._init_body_text_partition()

    def __repr__(self) -> str:
        return str(self.json)

    def iterate_on_parts(self) -> Tuple[Iterator[Any], int]:
        idx = 0
        for part in self.json['parts']:
            yield part, idx
            idx = idx + 1

    def iterate_on_sections(self) -> Tuple[Iterator[Any], Tuple[int, int]]:
        for part, part_idx in self.iterate_on_parts():
            idx = 0
            for section in part['sections']:
                yield section, (part_idx, idx)
                idx = idx + 1

    def iterate_on_boxes(self) -> Tuple[Box, BoxRef]:
        for section, [part_idx, section_idx_loc] in self.iterate_on_sections():
            for e in range(4):
                idx = 0
                for box_json in section[evangelists[e]]:
                    if box_json:
                        yield Box(box_json, e), BoxRef(part_idx, section_idx_loc, section['id'], e, idx)
                    idx = idx + 1

    def iterate_on_main_boxes(self) -> Tuple[Box, BoxRef]:
        for box, ref in self.iterate_on_boxes():
            if box and box.json['leading']:
                yield box, ref

    def iterate_on_parallel_boxes(self) -> Tuple[Box, BoxRef]:
        for box, ref in self.iterate_on_boxes():
            if box and not box.json['leading']:
                yield box, ref

    def iterate_on_all_biblical_text(self) -> Tuple[BibleRef, str]:
        for box, box_ref in self.iterate_on_boxes():
            for ref, t in box.iterate():
                if t:
                    yield ref, t


    def iterate_on_section_titles(self) -> str:
        for k, v in self.section_titles.items():
            yield v

    def iterate_on_part_titles(self) -> str:
        for t in self.part_titles:
            yield t

    def iterate_on_all_texts(self) -> str:
        for t in self.iterate_on_part_titles():
            yield t
        for t in self.iterate_on_section_titles():
            yield t
        for ref, t in self.iterate_on_all_biblical_text():
            yield t

    def get_box(self, ref: BoxRef) -> Box:
        return Box(self.json['parts'][ref.part_idx]['sections'][ref.section_idx_loc][evangelists[ref.e]][ref.idx], ref)

    def get_text(self, ref: BibleRef) -> str:
        return self.ref_to_text[ref]

    def get_name(self) -> str:
        return self.json['translation']

    def get_cut_verses(self) -> list[BibleRef]:
        ret = []
        for box, box_ref in self.iterate_on_boxes():
            for bible_ref, text in box.iterate():
                if bible_ref.is_cut_ref():
                    ret.append(bible_ref.get_base_ref())
        return sorted(set(ret))

    def get_cut_main_verses(self) -> list[BibleRef]:
        ret = []
        for box, box_ref in self.iterate_on_main_boxes():
            b = Box(box, box_ref.e)
            for bible_ref, text in b.iterate():
                if bible_ref.is_cut_ref():
                    ret.append(bible_ref.get_base_ref())
        return sorted(set(ret))

    def _init_section_titles(self):
        start = True
        prev = 0
        for section, section_idx_loc in self.iterate_on_sections():
            id_str = section['id']
            assert id_str.isdigit()
            assert id_str not in self.section_titles
            if start:
                start = False
            else:
                assert prev < int(id_str), f'Section id should increase. prev={prev} curr={int(id_str)}'
            assert int(id_str) <= 367, f'Section id should be maximum 367. curr={int(id_str)}'
            prev = start
            self.section_titles[id_str] = section['section_title']

    def _init_ref_to_text(self):
        rt = self.ref_to_text
        for box, box_ref in self.iterate_on_boxes():
            for bible_ref, text in box.iterate():
                if bible_ref in rt:
                    assert rt[
                               bible_ref] == text, f'Verse {bible_ref} with multiple texts in {self.get_name()}:\ntext_1={rt[bible_ref]}\ntext_2={text}'
                else:
                    self.ref_to_text[bible_ref] = text
        cut_verses = self.get_cut_verses()
        for v in cut_verses:
            a = BibleRef(v.e, v.chapter, v.verse, 1)
            b = BibleRef(v.e, v.chapter, v.verse, 2)
            if a in rt and b in rt and v in rt:
                concat = rt[a] + ' ' + rt[b]
                assert rt[
                           v] == concat, f'Cut verse a + b failure in {self.get_name()}:\n{a}={rt[a]}\n{b}={rt[b]}\n{v} ={rt[v]}'
            elif a in self.ref_to_text and b in self.ref_to_text:
                rt[v] = rt[a] + ' ' + rt[b]
            elif a in rt and v in rt:
                assert rt[v].startswith(
                    rt[a]), f'Cut verse prefix failure in {self.get_name()}:\n{a}={rt[a]}\n{v} ={rt[v]}'
                rt[b] = rt[v][(len(rt[a]) + 1):]
            elif b in rt and v in rt:
                assert rt[v].endswith(
                    rt[b]), f'Cut verse suffix failure in {self.get_name()}:\n{b}={rt[b]}\n{v} ={rt[v]}'
                rt[a] = rt[v][: -(len(rt[b]) + 1)]
            else:
                c = a if a in rt else b
                assert False, f'Isolated cut verse in {self.get_name()}: verse{c}. A pair or a base verse should exist.'

    def _init_body_ref_to_box_ref(self):
        for box, box_ref in self.iterate_on_main_boxes():
            for bible_ref, text in box.iterate():
                assert bible_ref not in self.body_ref_to_box_ref, f'Body text verse not unique. verse={bible_ref}'
                self.body_ref_to_box_ref[bible_ref] = box_ref

    def _init_body_text_partition(self):
        for box, box_ref in self.iterate_on_main_boxes():
            first, last = BibleRef.end(), BibleRef.end()
            for index, (bible_ref, text) in enumerate(box.iterate()):
                if index == 0:
                    first = bible_ref
                last = bible_ref
            self.body_text_partition.append(BibleSec(first, last.next()))
        self.body_text_partition.sort(key=lambda x: x.begin)
