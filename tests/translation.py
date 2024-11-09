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
            yield BibleRef(self.e, int(v['chapter']), verse, x), v.text


class Translation:
    """Represents a bible translation"""

    def __init__(self, loaded_json):
        self.json: json = loaded_json
        self.part_titles: list[str] = []
        self.section_titles: dict[str, str] = {}
        self.ref_to_text: dict[BibleRef, str] = {}
        self.body_ref_to_box_ref: dict[BibleRef, BoxRef] = {}
        self.body_text_partition: list[BibleSec] = []

        for part in self.iterate_on_parts():
            self.part_titles.append(part['part_title'])

        for section in self.iterate_on_sections():
            id_str = section['id']
            assert id_str.isdigit()
            assert id_str not in self.section_titles
            self.section_titles[id_str] = section['section_title']



    def __repr__(self) -> str:
        return str(self.json)

    def iterate_on_parts(self) -> Iterator[json]:
        for part in self.json['parts']:
            yield part

    def iterate_on_sections(self) -> Iterator[json]:
        for part in self.iterate_on_parts():
            for section in part['sections']:
                yield section

    def iterate_on_boxes(self) -> Iterator[json]:
        for section in self.iterate_on_sections():
            for evangelist in evangelists:
                for box in section[evangelist]:
                    if box:
                        yield box

    def iterate_on_main_boxes(self) -> Iterator[json]:
        for box in self.iterate_on_boxes():
            if box and box['leading']:
                yield box


    def get_box(self, ref: BoxRef) -> Box:
        return Box(self.json['parts'][ref.part_idx]['sections'][ref.section_idx_loc][evangelists[ref.e]][ref.idx], ref)
