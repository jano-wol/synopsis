from functools import total_ordering

from file_utils import load_json


@total_ordering
class BibleRef:
    evangelist_list: list[str] = ['mt', 'mk', 'lk', 'jn']
    evangelist_dict: dict[str, int] = {}
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
        return (self._get_evangelist_idx(), self.chapter, self.verse, self.x) == (
            other._get_evangelist_idx(), other.chapter, other.verse, other.x)

    def __lt__(self, other: 'BibleRef') -> bool:
        idx1 = self._get_idx()
        idx2 = other._get_idx()
        return idx1 < idx2

    def __hash__(self):
        return hash((self.evangelist, self.chapter, self.verse, self.x))

    @classmethod
    def class_init(cls, json_folder_path):
        if not cls.evangelist_dict:
            for idx, book in enumerate(cls.evangelist_list):
                cls.evangelist_dict[book] = idx
        if not cls.bible_ref_dict:
            bible_path = json_folder_path + '/' + 'kg.json'  # json_test.py assures that any translation can be chosen
            bible = load_json(bible_path)
            BibleRef._get_bible_refs(bible)
            for idx, ref in enumerate(cls.bible_ref_list):
                cls.bible_ref_dict[ref] = idx

    @classmethod
    def from_repr(cls, repr_str) -> 'BibleRef':
        parts = repr_str.split(",")
        evangelist = parts[0][0:2]
        chapter=int(parts[0][2:])
        verse_str=parts[1]
        if verse_str[-1].isdigit():
            verse = int(verse_str)
            x = ''
        else:
            verse = int(verse_str[:-1])
            x = verse_str[-1]
        return BibleRef(evangelist, chapter, verse, x)

    def next(self) -> 'BibleRef':
        idx = self._get_idx() + 1
        if self.x == '':
            while BibleRef.bible_ref_list[idx].x != '':
                idx = idx + 1
        return BibleRef.bible_ref_list[idx]

    def _get_evangelist_idx(self) -> int:
        return BibleRef.evangelist_dict[self.evangelist]

    def _get_idx(self) -> int:
        return BibleRef.bible_ref_dict[self]

    @staticmethod
    def _get_bible_refs(bible):
        for evangelist in BibleRef.evangelist_list:
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
                                    if verse_str[-1].isdigit():
                                        BibleRef.bible_ref_list.append(
                                            BibleRef(evangelist, int(v['chapter']), int(v['verse']), ''))
                                    else:
                                        BibleRef.bible_ref_list.append(
                                            BibleRef(evangelist, int(v['chapter']), int(v['verse'][:-1]), v['verse'][-1]))
