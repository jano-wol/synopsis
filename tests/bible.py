from functools import total_ordering
from typing import Tuple

# @formatter:off
evangelists = ['mt', 'mk', 'lk', 'jn']
lengths = {
    'mt': [25, 23, 17, 25, 48, 34, 29, 34, 38, 42, 30, 50, 58, 36, 39, 28, 27, 35, 30, 34, 46, 46, 39, 51, 46, 75, 66, 20],
    'mk': [45, 28, 35, 41, 43, 56, 37, 38, 50, 52, 33, 44, 37, 72, 47, 20],
    'lk': [80, 52, 38, 44, 39, 49, 50, 56, 62, 42, 54, 59, 35, 35, 32, 31, 37, 43, 48, 47, 38, 71, 56, 53],
    'jn': [51, 	25, 36, 54, 47, 71, 53, 59, 41, 42, 57, 50, 38, 31, 27, 33, 26, 40, 42, 31, 25]
}
# @formatter:on


def get_number_of_chapters(evangelist):
    return len(lengths[evangelist])


def get_number_of_verses(evangelist, chapter):
    return lengths[evangelist][chapter - 1]


@total_ordering
class BibleRef:
    """Represents a gospel reference with evangelist, chapter, verse, and optional notes, e.g., mt5,38 or jn19,16a"""

    def __init__(self, e: int, chapter: int, verse: int, x: int):
        self.e = e
        self.chapter = chapter
        self.verse = verse
        self.x = x

    def __repr__(self) -> str:
        s = ''
        if self.x == 1:
            s = 'a'
        if self.x == 2:
            s = 'b'
        return f'{evangelists[self.e]}{self.chapter},{self.verse}{s}'

    def __eq__(self, other: 'BibleRef') -> bool:
        return (self.e, self.chapter, self.verse, self.x) == (
            other.e, other.chapter, other.verse, other.x)

    def __lt__(self, other: 'BibleRef') -> bool:
        return (self.e, self.chapter, self.verse, self.x) < (
            other.e, other.chapter, other.verse, other.x)

    def __hash__(self) -> int:
        return hash((self.e, self.chapter, self.verse, self.x))

    def next(self) -> 'BibleRef':
        assert self != BibleRef.end(), 'next called on end'
        if self.x == 1:
            return BibleRef(self.e, self.chapter, self.verse, 2)
        else:
            v = get_number_of_verses(evangelists[self.e], self.chapter)
            if self.verse != v:
                return BibleRef(self.e, self.chapter, self.verse + 1, 0)
            c = get_number_of_chapters(evangelists[self.e])
            if self.chapter != c:
                return BibleRef(self.e, self.chapter + 1, 1, 0)
            if self.e != 3:
                return BibleRef(self.e + 1, 1, 1, 0)
            else:
                return BibleRef(self.e, 99, 99, 0)

    def is_cut_ref(self) -> bool:
        return self.x != 0

    def get_base_ref(self) -> 'BibleRef':
        return BibleRef(self.e, self.chapter, self.verse, 0)

    @staticmethod
    def begin() -> 'BibleRef':
        return BibleRef(0, 1, 1, 0)

    @staticmethod
    def end() -> 'BibleRef':
        return BibleRef(3, 99, 99, 0)

    @staticmethod
    def from_string(repr_str: str) -> 'BibleRef':
        """Parses a reference string in the form 'mt5,38' or 'jn19,16b'"""
        parts = repr_str.split(",")
        e = evangelists.index(parts[0][0:2])
        chapter = int(parts[0][2:])
        verse_str = parts[1]
        verse, x = BibleRef.split_verse(verse_str)
        return BibleRef(e, chapter, verse, x)

    @staticmethod
    def split_verse(verse_str: str) -> Tuple[int, int]:
        """Splits '16' into [16, 0], '16a' into [16, 1] and '16b' into [16, 2]"""
        if verse_str[-1].isdigit():
            verse = int(verse_str)
            x = 0
        else:
            verse = int(verse_str[:-1])
            x = 1 if verse_str[-1] == 'a' else 2
        return verse, x


class BibleSec:
    """Represents consecutive gospel verses as [start, end), with start and end as BibleRef objects"""
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
        """If end is inclusive, adjusts self to be a left-closed, right-open interval"""
        self.end = self.end.next()

    def intersect(self, other: 'BibleSec') -> 'BibleSec':
        if self.is_empty():
            return self
        if other.is_empty():
            return other
        start = max(self.start, other.start)
        end = min(self.end, other.end)
        return BibleSec(start, end)

    def is_intersect(self, other: 'BibleSec') -> bool:
        return not self.intersect(other).is_empty()

    @classmethod
    def from_closed_string(cls, closed_str: str) -> 'BibleSec':
        """ 'lk5,5'->[lk5,5;lk5,6), 'mk9,43-48'->[mk9,43;mk9,49), 'mk9,43-50'->[mk9,43;mk10,1),
            'mk9,43-10,2'->[mk9,43;mk10,3), 'mk1,1-6,6a'->[mk1,1;mk6,6b), 'mt8,11-mk6,6b'->[mt8,11;mk6,7),
            'jn1,1-mk6,6'->[jn1,1;mk6,7), 'mt8,11-lk24,53'->[mt8,11;jn1,1), 'mt1,1-jn21,25'->[mt1,1;jn99,99) """
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
                    end = BibleRef(start.e, chapter, verse, x)
                else:
                    end = BibleRef.from_string(str_2)
            else:
                verse, x = BibleRef.split_verse(str_2)
                end = BibleRef(start.e, start.chapter, verse, x)
        else:
            start = BibleRef.from_string(closed_str)
            end = BibleRef.from_string(closed_str)
        return BibleSec(start, end.next())
