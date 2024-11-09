import json

from typing import Iterator, Tuple

from bible import BibleRef, BibleSec, evangelists


class BoxRef:
    """Represents a box reference in a translation"""

    def __init__(self, part_idx: int, section_idx_loc: int, section_id: int, e: int, idx: int):
        self.part_idx = part_idx
        self.section_idx_loc = section_idx_loc
        self.section_id = section_id
        self.e = e
        self.idx = idx

    def __repr__(self) -> str:
        return f'({self.part_idx};{self.section_id};{evangelists[self.e]};{self.idx})'


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
            verse_str = v['verse']
            verse, x = BibleRef.split_verse(verse_str)
            yield BibleRef(self.e, int(v['chapter']), verse, x), v['text']


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

        for section, section_idx_loc in self.iterate_on_sections():
            id_str = section['id']
            assert id_str.isdigit()
            assert id_str not in self.section_titles
            self.section_titles[id_str] = section['section_title']

        for box, box_ref in self.iterate_on_boxes():
            b = Box(box, box_ref.e)
            for bible_ref, text in b.iterate():
                if bible_ref in self.ref_to_text:
                    if self.ref_to_text[bible_ref] != text:
                        print(
                            f'Same ref, different text failure.\ntext_1={self.ref_to_text[bible_ref]}\ntext_2={text}\nverse={bible_ref} translation={self.get_name()}')
                else:
                    self.ref_to_text[bible_ref] = text
        cut_verses = self.get_cut_verses()
        for v in cut_verses:
            a = BibleRef(v.e, v.chapter, v.verse, 1)
            b = BibleRef(v.e, v.chapter, v.verse, 2)
            concat = self.ref_to_text[a] + ' ' + self.ref_to_text[b]
            if v in self.ref_to_text:
                if self.ref_to_text[v] != concat:
                    print(f'Cut verse a + b failure.\ntext_1={self.ref_to_text[v]}\nconcat={concat}\nverse={v} translation={self.get_name()}')
            else:
                self.ref_to_text[v] = concat

        for box, box_ref in self.iterate_on_main_boxes():
            b = Box(box, box_ref.e)
            for bible_ref, text in b.iterate():
                assert bible_ref not in self.body_ref_to_box_ref
                self.body_ref_to_box_ref[bible_ref] = box_ref

        for box, box_ref in self.iterate_on_main_boxes():
            b = Box(box, box_ref.e)
            first, last = BibleRef.end(), BibleRef.end()
            for index, (bible_ref, text) in enumerate(b.iterate()):
                if index == 0:
                    first = bible_ref
                last = bible_ref
            self.body_text_partition.append(BibleSec(first, last.next()))
        self.body_text_partition.sort(key=lambda x: x.start)

    def __repr__(self) -> str:
        return str(self.json)

    def iterate_on_parts(self) -> Tuple[Iterator[json], int]:
        idx = 0
        for part in self.json['parts']:
            yield part, idx
            idx = idx + 1

    def iterate_on_sections(self) -> Tuple[Iterator[json], Tuple[int, int]]:
        for part, part_idx in self.iterate_on_parts():
            idx = 0
            for section in part['sections']:
                yield section, (part_idx, idx)
                idx = idx + 1

    def iterate_on_boxes(self) -> Tuple[Iterator[json], BoxRef]:
        for section, [part_idx, section_idx_loc] in self.iterate_on_sections():
            for e in range(4):
                idx = 0
                for box in section[evangelists[e]]:
                    if box:
                        yield box, BoxRef(part_idx, section_idx_loc, section['id'], e, idx)
                    idx = idx + 1

    def iterate_on_main_boxes(self) -> Tuple[Iterator[json], BoxRef]:
        for box, ref in self.iterate_on_boxes():
            if box and box['leading']:
                yield box, ref

    def get_box(self, ref: BoxRef) -> Box:
        return Box(self.json['parts'][ref.part_idx]['sections'][ref.section_idx_loc][evangelists[ref.e]][ref.idx], ref)

    def get_text(self, ref: BibleRef) -> str:
        return self.ref_to_text[ref]

    def get_name(self) -> str:
        return self.json['translation']

    def get_cut_verses(self):
        ret = []
        for box, box_ref in self.iterate_on_boxes():
            b = Box(box, box_ref.e)
            for bible_ref, text in b.iterate():
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
