from typing import Tuple
import sys

from bible_ref import BibleRef, BibleSec
from file_utils import load_json

evangelists = ['mt', 'mk', 'lk', 'jn']


def get_body_text_intervals(bible_json) -> list[Tuple[BibleSec, int]]:
    ret = []
    for evangelist in evangelists:
        for p in bible_json['parts']:
            for section in p['sections']:
                id_1 = int(section['id'])
                for box in section[evangelist]:
                    if box and box['leading']:
                        chapter_str_1 = box['content'][0]['chapter']
                        verse_str_1 = box['content'][0]['verse']
                        chapter_str_2 = box['content'][-1]['chapter']
                        verse_str_2 = box['content'][-1]['verse']
                        str_1 = f'{evangelist}{chapter_str_1},{verse_str_1}'
                        str_2 = f'{evangelist}{chapter_str_2},{verse_str_2}'
                        start = BibleRef.from_string(str_1)
                        end = BibleRef.from_string(str_2)
                        sec = BibleSec(start, end)
                        sec.fix_close_sec()
                        ret.append((sec, id_1))
    return ret


def main():
    redirect_folder = sys.argv[1]
    translation_folder = sys.argv[2]
    BibleRef.class_init(translation_folder)
    bible_path = translation_folder + '/' + 'kg.json'
    bible_json = load_json(bible_path)
    print(BibleRef.bible_ref_list)
    body_text_intervals = get_body_text_intervals(bible_json)
    print(body_text_intervals)
    to_leading_path = redirect_folder + '/' + 'toLeading.json'
    to_leading_json = load_json(to_leading_path)
    for e in to_leading_json:
        sec = BibleSec.from_closed_string(e)


if __name__ == '__main__':
    main()
