import bisect
import os
import sys
from typing import Tuple

from bible import BibleRef, BibleSec, evangelists
from file_utils import iterate_jsons, load_json
from translation import Box, BoxRef, Translation

leading_file_name = 'toLeading.json'
next_file_name = 'toNext.json'
previous_file_name = 'toPrevious.json'


def get_redirect_file_path(redirect_folder, file_name):
    return os.path.join(redirect_folder, file_name)


def get_possible_lead_sections(parallel_section_str, translation):
    body_text_rights = [el.end for el in translation.body_text_partition]
    sec = BibleSec.from_closed_string(parallel_section_str)
    start = sec.begin
    index = bisect.bisect_right(body_text_rights, start)
    assert translation.body_text_partition[index].is_intersect(sec)
    if index > 0:
        assert not translation.body_text_partition[index - 1].is_intersect(sec)
    possible_lead_sections = set()
    while index < len(translation.body_text_partition) and translation.body_text_partition[index].is_intersect(sec):
        possible_lead_sections.add(
            int(translation.body_ref_to_box_ref[translation.body_text_partition[index].begin].section_id))
        index = index + 1
    return possible_lead_sections


def test_leading(redirect_folder, translation):
    to_leading_path = get_redirect_file_path(redirect_folder, leading_file_name)
    to_leading_json = load_json(to_leading_path)
    for parallel_section_str, lead_section in to_leading_json.items():
        possible_lead_sections = get_possible_lead_sections(parallel_section_str, translation)
        assert lead_section in possible_lead_sections
        if len(possible_lead_sections) > 1:
            print(f'{parallel_section_str} {possible_lead_sections}')

    for box, box_ref in translation.iterate_on_parallel_boxes():
        # assert box.get_closed_str() in to_leading_json, f'str={box.get_closed_str()} box_ref={box_ref}'
        pass


def test_neighbourhood(redirect_folder, translation):
    next_path = get_redirect_file_path(redirect_folder, next_file_name)
    previous_path = get_redirect_file_path(redirect_folder, previous_file_name)
    next_json = load_json(next_path)
    previous_json = load_json(previous_path)
    main_body_counts = 4 * [0]
    for sec in translation.body_text_partition:
        main_body_counts[sec.begin.e] = main_body_counts[sec.begin.e] + 1

    for e in range(4):
        index = 0
        for box, box_ref in translation.iterate_on_main_boxes():
            if box.e == e:
                if index != 0:
                    assert box.get_closed_str() in previous_json, f'str={box.get_closed_str()} not found in {previous_file_name} box_ref={box_ref}'
                if index != main_body_counts[e] - 1:
                    assert box.get_closed_str() in next_json, f'str={box.get_closed_str()} not found in {next_file_name} box_ref={box_ref}'
                index = index + 1

def main():
    translation_folder = sys.argv[1]
    redirect_folder = sys.argv[2]
    bible_json, _ = next(iterate_jsons(translation_folder))
    translation = Translation(bible_json)
    test_leading(redirect_folder, translation)
    test_neighbourhood(redirect_folder, translation)


if __name__ == '__main__':
    main()
