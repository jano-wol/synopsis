from functools import total_ordering

from file_utils import load_json


@total_ordering
class BibleRef:
    book_list: list[str] = ['mt', 'mk', 'lk', 'jn']
    book_dict: dict[str, int] = {}
    bible_ref_list: list['BibleRef'] = []
    bible_ref_dict: dict['BibleRef', int] = {}

    def __init__(self, book: str, chapter: int, verse: int, x: str):
        self.book = book
        self.chapter = chapter
        self.verse = verse
        self.x = x

    def __repr__(self) -> str:
        return f'{self.book}{self.chapter},{self.verse}{self.x}'

    def __eq__(self, other: 'BibleRef') -> bool:
        return (self._get_book_idx(), self.chapter, self.verse, self.x) == (
            other._get_book_idx(), other.chapter, other.verse, other.x)

    def __lt__(self, other: 'BibleRef') -> bool:
        idx1 = self._get_idx()
        idx2 = other._get_idx()
        return idx1 < idx2

    def __hash__(self):
        return hash((self.book, self.chapter, self.verse, self.x))

    @classmethod
    def class_init(cls, json_folder_path):
        if not cls.book_dict:
            for idx, book in enumerate(cls.book_list):
                cls.book_dict[book] = idx
        if not cls.bible_ref_dict:
            bible_path = json_folder_path + '/' + 'kg.json'  # json_test.py assures that any translation can be chosen
            bible = load_json(bible_path)
            BibleRef._get_bible_refs(bible)
            for idx, ref in enumerate(cls.bible_ref_list):
                cls.bible_ref_dict[ref] = idx

    def next(self) -> 'BibleRef':
        idx = self._get_idx() + 1
        if self.x == '':
            while BibleRef.bible_ref_list[idx].x != '':
                idx = idx + 1
        return BibleRef.bible_ref_list[idx]

    def _get_book_idx(self) -> int:
        return BibleRef.book_dict[self.book]

    def _get_idx(self) -> int:
        return BibleRef.bible_ref_dict[self]

    @staticmethod
    def _get_bible_refs(bible):
        for book in BibleRef.book_list:
            for p in bible['parts']:
                for section in p['sections']:
                    for box in section[book]:
                        if box and box['leading']:
                            for v in box['content']:
                                verse_str = v['verse']
                                if verse_str[-1] == 'a':
                                    BibleRef.bible_ref_list.append(
                                        BibleRef(book, int(v['chapter']), int(v['verse'][:-1]), ''))
                                    BibleRef.bible_ref_list.append(
                                        BibleRef(book, int(v['chapter']), int(v['verse'][:-1]), 'a'))
                                else:
                                    if verse_str[-1].isdigit():
                                        BibleRef.bible_ref_list.append(
                                            BibleRef(book, int(v['chapter']), int(v['verse']), ''))
                                    else:
                                        BibleRef.bible_ref_list.append(
                                            BibleRef(book, int(v['chapter']), int(v['verse'][:-1]), v['verse'][-1]))
