import bisect
import os
import sys

from bible import BibleSec
from file_utils import iterate_jsons, load_json
from translation import Translation

leading_file_name = 'toLeading.json'
next_file_name = 'toNext.json'
previous_file_name = 'toPrevious.json'


def get_redirect_file_path(redirect_folder, file_name):
    return os.path.join(redirect_folder, file_name)


def get_possible_lead_sections(parallel_section_str, translation, body_text_rights):
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
    body_text_rights = [el.end for el in translation.body_text_partition]
    for parallel_section_str, lead_section in to_leading_json.items():
        possible_lead_sections = get_possible_lead_sections(parallel_section_str, translation, body_text_rights)
        assert lead_section in possible_lead_sections, f'{parallel_section_str} lead is expected to be in {possible_lead_sections}. curr_val={lead_section}'
        # if len(possible_lead_sections) > 1:
        #    print(f'{parallel_section_str} {possible_lead_sections}')

    used_keys = set()
    all_keys = set(to_leading_json.keys())
    for box, box_ref in translation.iterate_on_parallel_boxes():
        closed_str = box.get_closed_str()
        assert closed_str in to_leading_json, f'Leading was not found for str={closed_str} box_ref={box_ref}. Possible values={get_possible_lead_sections(closed_str, translation, body_text_rights)}'
        used_keys.add(closed_str)
    unused_keys = all_keys - used_keys
    assert not unused_keys, f'Unused keys found in {leading_file_name}. unused_keys={unused_keys}'


def find_index(target, sorted_list):
    index = bisect.bisect_left(sorted_list, target)
    assert index < len(sorted_list) and sorted_list[index] == target, f'{target} was not found as main body begin.'
    return index


def test_main_body_neighbours(redirect_folder, translation):
    next_path = get_redirect_file_path(redirect_folder, next_file_name)
    previous_path = get_redirect_file_path(redirect_folder, previous_file_name)
    next_json = load_json(next_path)
    previous_json = load_json(previous_path)
    main_body_counts = 4 * [0]
    for sec in translation.body_text_partition:
        main_body_counts[sec.begin.e] = main_body_counts[sec.begin.e] + 1

    used_keys_next = set()
    used_keys_prev = set()
    all_keys_next = set(next_json.keys())
    all_keys_prev = set(previous_json.keys())
    for e in range(4):
        index = 0
        for box, box_ref in translation.iterate_on_main_boxes():
            if box.e == e:
                closed_str = box.get_closed_str()
                if index != 0:
                    assert closed_str in previous_json, f'str={closed_str} not found in {previous_file_name} box_ref={box_ref}'
                    used_keys_prev.add(closed_str)
                if index != main_body_counts[e] - 1:
                    assert closed_str in next_json, f'str={closed_str} not found in {next_file_name} box_ref={box_ref}'
                    used_keys_next.add(closed_str)
                index = index + 1
    unused_keys_next = all_keys_next - used_keys_next
    unused_keys_prev = all_keys_prev - used_keys_prev
    assert not unused_keys_next, f'Unused keys found in {next_file_name}. unused_keys={unused_keys_next}'
    assert not unused_keys_prev, f'Unused keys found in {previous_file_name}. unused_keys={unused_keys_prev}'

    body_text_lefts = [el.begin for el in translation.body_text_partition]
    for main_body_str, v_json in next_json.items():
        sec = BibleSec.from_closed_string(main_body_str)
        index = find_index(sec.begin, body_text_lefts)
        v_calc = int(translation.body_ref_to_box_ref[body_text_lefts[index + 1]].section_id)
        assert v_json == v_calc, f'Next failed for {main_body_str} v_json={v_json} v_calc={v_calc}'

    for main_body_str, v_json in previous_json.items():
        sec = BibleSec.from_closed_string(main_body_str)
        index = find_index(sec.begin, body_text_lefts)
        v_calc = int(translation.body_ref_to_box_ref[body_text_lefts[index - 1]].section_id)
        assert v_json == v_calc, f'Previous failed for {main_body_str} v_json={v_json} v_calc={v_calc}'


def main():
    translation_folder = sys.argv[1]
    redirect_folder = sys.argv[2]
    bible_json, _ = next(iterate_jsons(translation_folder))
    translation = Translation(bible_json)

    test_leading(redirect_folder, translation)
    test_main_body_neighbours(redirect_folder, translation)


if __name__ == '__main__':
    main()
