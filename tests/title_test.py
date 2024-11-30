import os
import re
import sys

from bible import evangelists
from file_utils import iterate_jsons

roman = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI',
                 'XVII', 'XVIII']


def remove_roman_literal(title):
    roman_numeral_pattern = r'^\s*(?=[MDCLXVI])M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})(\.?\s*)'
    cleaned_title = re.sub(roman_numeral_pattern, '', title)
    return cleaned_title.strip()


def check_part_titles(json_loaded, file_name):
    seen_part_titles = set()
    part_id = 1
    for p in json_loaded['parts']:
        part_title = p['part_title']
        assert p['part_title'].startswith(roman[part_id - 1]), f'Starting roman numeral mismatch. part_title={part_title}'
        part_title = remove_roman_literal(p['part_title'])
        if part_title in seen_part_titles:
            print(f'Duplicate part_title found: {part_title}. file_name={file_name}')
            exit(1)
        else:
            seen_part_titles.add(part_title)
        part_id = part_id + 1


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
    json_folder = sys.argv[1]
    json_files_found = False
    for json_loaded, json_path in iterate_jsons(json_folder):
        json_files_found = True
        file_name = os.path.basename(json_path)
        check_translation(json_loaded, file_name)
    if not json_files_found:
        print(f'No json files were found in folder={json_folder}')
        sys.exit(1)


if __name__ == '__main__':
    main()
