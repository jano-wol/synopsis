from functools import total_ordering
from typing import Tuple

from file_utils import iterate_jsons


@total_ordering
class BibleRef:
    bible_ref_list: list['BibleRef'] = []
    bible_ref_dict: dict['BibleRef', int] = {}

    def __init__(self, evangelist: str, chapter: int, verse: int, x: str):
        self.evangelist = evangelist
        self.chapter = chapter
        self.verse = verse
        self.x = x

    def __repr__(self) -> str:
        return f'{self.evangelist}{self.chapter},{self.verse}{self.x}'

    def __eq__(self, other: 'BibleRef') -> bool:
        return (self.evangelist, self.chapter, self.verse, self.x) == (
            other.evangelist, other.chapter, other.verse, other.x)

    def __lt__(self, other: 'BibleRef') -> bool:
        idx1 = self._get_idx()
        idx2 = other._get_idx()
        return idx1 < idx2

    def __hash__(self):
        return hash((self.evangelist, self.chapter, self.verse, self.x))

    @classmethod
    def class_init(cls, json_folder_path: str):
        if not cls.bible_ref_dict:
            bible, _ = next(iterate_jsons(json_folder_path))
            BibleRef._get_bible_refs(bible)

            # add end element
            a = BibleRef.bible_ref_list[-1]
            BibleRef.bible_ref_list.append(BibleRef(a.evangelist, 99, 99, ''))

            # init bible_ref_dict
            for idx, ref in enumerate(cls.bible_ref_list):
                cls.bible_ref_dict[ref] = idx

    def next(self) -> 'BibleRef':
        idx = self._get_idx() + 1
        if self.x == '':
            while BibleRef.bible_ref_list[idx].x != '':
                idx = idx + 1
        return BibleRef.bible_ref_list[idx]

    @staticmethod
    def from_string(repr_str: str) -> 'BibleRef':
        parts = repr_str.split(",")
        evangelist = parts[0][0:2]
        chapter = int(parts[0][2:])
        verse_str = parts[1]
        verse, x = BibleRef.split_verse(verse_str)
        return BibleRef(evangelist, chapter, verse, x)

    @staticmethod
    def split_verse(verse_str: str) -> Tuple[int, str]:
        if verse_str[-1].isdigit():
            verse = int(verse_str)
            x = ''
        else:
            verse = int(verse_str[:-1])
            x = verse_str[-1]
        return verse, x

    def _get_idx(self) -> int:
        return BibleRef.bible_ref_dict[self]

    @staticmethod
    def _get_bible_refs(bible):
        for evangelist in ['mt', 'mk', 'lk', 'jn']:
            for p in bible['parts']:
                for section in p['sections']:
                    for box in section[evangelist]:
                        if box and box['leading']:
                            for v in box['content']:
                                verse_str = v['verse']
                                if verse_str[-1] == 'a':
                                    BibleRef.bible_ref_list.append(
                                        BibleRef(evangelist, int(v['chapter']), int(v['verse'][:-1]), ''))
                                    BibleRef.bible_ref_list.append(
                                        BibleRef(evangelist, int(v['chapter']), int(v['verse'][:-1]), 'a'))
                                else:
                                    verse, x = BibleRef.split_verse(verse_str)
                                    BibleRef.bible_ref_list.append(BibleRef(evangelist, int(v['chapter']), verse, x))


class BibleSec:
    start: BibleRef
    end: BibleRef

    def __init__(self, start: BibleRef, end: BibleRef):
        self.start = start
        self.end = end

    def __repr__(self) -> str:
        return f'[{self.start};{self.end})'

    def __eq__(self, other: 'BibleSec') -> bool:
        return (self.start, self.end) == (other.start, other.end)

    def __hash__(self):
        return hash((self.start, self.end))

    def is_empty(self) -> bool:
        return self.end <= self.start

    def fix_closed(self):
        self.end = self.end.next()

    def intersect(self, other: 'BibleSec') -> 'BibleSec':
        if self.is_empty() or other.is_empty():
            return self
        start = max(self.start, other.start)
        end = min(self.end, other.end)
        return BibleSec(start, end)

    def is_intersect(self, other: 'BibleSec') -> bool:
        return not self.intersect(other).is_empty()

    @classmethod
    def from_closed_string(cls, closed_str: str) -> 'BibleSec':
        if '-' in closed_str:
            str_1 = closed_str.split('-', 1)[0]
            start = BibleRef.from_string(str_1)
            str_2 = closed_str.split('-', 1)[1]
            if ',' in str_2:
                start_2_1 = str_2.split(',', 1)[0]
                start_2_2 = str_2.split(',', 1)[1]
                if start_2_1[0].isdigit():
                    chapter = int(start_2_1)
                    verse, x = BibleRef.split_verse(start_2_2)
                    end = BibleRef(start.evangelist, chapter, verse, x)
                else:
                    end = BibleRef.from_string(str_2)
            else:
                verse, x = BibleRef.split_verse(str_2)
                end = BibleRef(start.evangelist, start.chapter, verse, x)
        else:
            start = BibleRef.from_string(closed_str)
            end = BibleRef.from_string(closed_str)
        return BibleSec(start, end.next())
