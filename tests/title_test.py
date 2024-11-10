import os
import re
import sys

from bible import evangelists
from file_utils import iterate_jsons

checked_translations = ['kg', 'esv', 'szit', 'knb', 'bt', 'bjw', 'rsp', 'nv', 'sblgnt', 'eu']


def remove_roman_literal(title):
    roman_numeral_pattern = r'^\s*(?=[MDCLXVI])M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})(\.?\s*)'
    cleaned_title = re.sub(roman_numeral_pattern, '', title)
    return cleaned_title.strip()


def check_part_titles(json_loaded, file_name):
    seen_part_titles = set()
    for p in json_loaded['parts']:
        part_title = remove_roman_literal(p['part_title'])
        if part_title in seen_part_titles:
            print(f'Duplicate part_title found: {part_title}. file_name={file_name}')
            exit(1)
        else:
            seen_part_titles.add(part_title)


def add_to_dict(check_section_titles_dict, section_title, main_body_counts):
    if section_title in check_section_titles_dict:
        check_section_titles_dict[section_title].append(main_body_counts)
    else:
        check_section_titles_dict[section_title] = [main_body_counts]


def get_main_body_counts(section):
    return [
        1 if any(box is not None and box['leading'] for box in section[evangelist])
        else 0
        for evangelist in evangelists
    ]


def check_section_titles(json_loaded, file_name):
    success = True
    check_section_titles_dict = {}
    for p in json_loaded['parts']:
        for section in p['sections']:
            section_title = section['section_title']
            main_body_counts = get_main_body_counts(section)
            add_to_dict(check_section_titles_dict, section_title, main_body_counts)
    for section_title, main_body_counts in check_section_titles_dict.items():
        summary = [sum(count[idx] for count in main_body_counts) for idx in range(4)]
        for idx, count in enumerate(summary):
            if count >= 2:
                print(
                    f'Repeated section titles found for different main bodies. file_name={file_name}; section_title={section_title}; Evangelist={evangelists[idx]}')
                success = False
    if not success:
        print('Section title test failed.')
        exit(1)


def check_translation(json_loaded, file_name):
    check_part_titles(json_loaded, file_name)
    check_section_titles(json_loaded, file_name)


def main():
    file_flags = {file_name: False for file_name in checked_translations}
    json_folder = sys.argv[1]
    for json_loaded, json_path in iterate_jsons(json_folder):
        file_name = os.path.basename(json_path)
        file_base_name = os.path.splitext(file_name)[0]
        if file_base_name in checked_translations:
            file_flags[file_base_name] = True
            check_translation(json_loaded, file_name)
    for file_name, tested in file_flags.items():
        if not tested:
            print(f'Test fail: {file_name}.json was not tested.')
            exit(1)


if __name__ == '__main__':
    main()
