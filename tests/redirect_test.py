import bisect
import os
import sys
from typing import Tuple

from bible import BibleRef, BibleSec, evangelists
from file_utils import iterate_jsons, load_json
from translation import Box, BoxRef, Translation

def main():
    translation_folder = sys.argv[1]
    redirect_folder = sys.argv[2]
    bible_json, _ = next(iterate_jsons(translation_folder))
    translation = Translation(bible_json)
    to_leading_path = os.path.join(redirect_folder, 'toLeading.json')
    to_leading_json = load_json(to_leading_path)
    #for e, v in to_leading_json.items():
    #    sec = BibleSec.from_closed_string(e)
    #    start = sec.start
    #    index = bisect.bisect_right(body_text_rights, start)
    #    assert body_text_intervals[index][0].is_intersect(sec)
    #    solutions = set()
    #    while index < len(body_text_intervals) and body_text_intervals[index][0].is_intersect(sec):
    #        solutions.add(body_text_intervals[index][1])
    #        index = index + 1
    #    assert v in solutions
    #    if len(solutions) > 1:
    #        print(f'{e} {solutions}')
    #r = BoxRef(17, 0, 363, 1, 0)
    #print(r)
    #translation = Translation(bible_json)
    print(translation.body_text_partition)
    #print(translation.get_box(r))

if __name__ == '__main__':
    main()
