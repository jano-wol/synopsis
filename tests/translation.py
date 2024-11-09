import json

from typing import Generator, Tuple

from bible import BibleRef, BibleSec, evangelists


class BoxRef:
    """Represents a box reference in a translation"""

    def __init__(self, part_idx: int, section_idx: int, e: int, idx: int):
        self.part_idx = part_idx
        self.section_idx = section_idx
        self.e = e
        self.idx = idx


class Box:

    def __init__(self, loaded_json, e):
        self.json: json = loaded_json
        self.e = e

    def is_body(self) -> bool:
        return self.json['leading']

    def iterate(self) -> Generator[Tuple[BibleRef, str], None, None]:
        for v in self.json['content']:
            verse_str = v['verse']
            verse, x = BibleRef.split_verse(verse_str)
            yield BibleRef(self.e, int(v['chapter']), verse, x), v.text


class Translation:
    """Represents a bible translation"""

    def __init__(self, loaded_json):
        self.json: json = loaded_json
        self.part_titles: list[str] = []
        self.section_titles: list[str] = []
        self.ref_to_text: dict[BibleRef, str] = {}
        self.body_ref_to_box_ref: dict[BibleRef, BoxRef] = {}
        self.body_text_partition: list[BibleSec] = []

    def iterate_on_all_boxes(self):
        pass

    def iterate_on_main_boxes(self):
        pass

    def get_box(self, ref: BoxRef) -> Box:
        return Box(self.json['parts'][ref.part_idx]['sections'][ref.section_idx][evangelists[ref.e]][ref.idx], ref)
