import os
import re
import sys

from file_utils import iterate_jsons

required_translations = ['kg', 'esv', 'szit']

def remove_roman_literal(title):
    roman_numeral_pattern = r'^\s*(?=[MDCLXVI])M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})(\.?\s*)'
    cleaned_title = re.sub(roman_numeral_pattern, '', title)
    return cleaned_title.strip()


def add_to_dict(check_dict, section_title, section_idx, leadings):
    if section_title in check_dict:
        check_dict[section_title][0].append(section_idx)
        check_dict[section_title][1].append(leadings)
    else:
        check_dict[section_title] = [[section_idx], [leadings]]


def check(json_loaded, file_name):
    success = True
    seen_part_titles = set()
    evangelists = ['mt', 'mk', 'lk', 'jn']
    section_idx = 0
    check_dict = {}
    for p in json_loaded['parts']:
        part_title = remove_roman_literal(p['part_title'])
        if part_title in seen_part_titles:
            print(f'Duplicate part_title found: {part_title}. file_name={file_name}')
            exit(1)
        else:
            seen_part_titles.add(part_title)
        for s in p['sections']:
            section_title = s['section_title']
            section_idx = section_idx + 1
            leadings = [0] * 4
            for idx in range(4):
                lead = 0
                boxes = s[evangelists[idx]]
                if boxes is not None:
                    for box in boxes:
                        if box is not None:
                            if box["leading"]:
                                lead = 1
                leadings[idx] = lead
            add_to_dict(check_dict, section_title, section_idx, leadings)
    for section_title, (section_indices, leadings) in check_dict.items():
        summarize = [0] * 4
        for leading in leadings:
            for idx in range(4):
                summarize[idx] = summarize[idx] + leading[idx]
        for idx in range(4):
            if summarize[idx] >= 2:
                print(
                    f'Multiple body texts under the same section_title from the same evangelist. file_name={file_name}; section_title={section_title}; evangelist={evangelists[idx]}')
                success = False
    if not success:
        print("Section title test failed.")
        exit(1)


def main():
    file_flags = {file_name: False for file_name in required_translations}
    json_folder = sys.argv[1]
    for json_loaded, json_path in iterate_jsons(json_folder):
        file_name = os.path.basename(json_path)
        file_base_name = os.path.splitext(file_name)[0]
        if file_base_name in required_translations:
            file_flags[file_base_name] = True
            check(json_loaded, file_name)
    for file_name, tested in file_flags.items():
        if not tested:
            print(f'Test fail: {file_name}.json was not tested.')
            exit(1)


if __name__ == '__main__':
    main()
