import bisect
import os
import sys
from typing import Tuple

from bible import BibleRef, BibleSec
from file_utils import iterate_jsons, load_json
from translation import Box, BoxRef, Translation

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
                        sec.fix_closed()
                        ret.append((sec, id_1))
    return ret


def main():
    redirect_folder = sys.argv[1]
    translation_folder = sys.argv[2]
    bible_json, _ = next(iterate_jsons(translation_folder))
    body_text_intervals = get_body_text_intervals(bible_json)
    body_text_rights = [el[0].end for el in body_text_intervals]
    to_leading_path = os.path.join(redirect_folder, 'toLeading.json')
    to_leading_json = load_json(to_leading_path)
    for e, v in to_leading_json.items():
        sec = BibleSec.from_closed_string(e)
        start = sec.start
        index = bisect.bisect_right(body_text_rights, start)
        assert body_text_intervals[index][0].is_intersect(sec)
        solutions = set()
        while index < len(body_text_intervals) and body_text_intervals[index][0].is_intersect(sec):
            solutions.add(body_text_intervals[index][1])
            index = index + 1
        assert v in solutions
        if len(solutions) > 1:
            print(f'{e} {solutions}')
    r = BoxRef(17, 0, 363, 1, 0)
    print(r)
    translation = Translation(bible_json)
    print(translation.body_text_partition)
    #print(translation.get_box(r))

    for b in translation.iterate_on_main_boxes():
        print(b)

if __name__ == '__main__':
    main()
