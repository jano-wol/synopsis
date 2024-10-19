import os
import re
import sys

from file_utils import iterate_jsons

def remove_roman_literal(title):
    roman_numeral_pattern = r'^\s*(?=[MDCLXVI])M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})(\.?\s*)'
    cleaned_title = re.sub(roman_numeral_pattern, '', title)
    return cleaned_title.strip()

def check(json_loaded, file_name):
    seen_part_titles = set()
    evangelists = ['mt', 'mk', 'lk', 'jn']
    for p in json_loaded['parts']:
        part_title = remove_roman_literal(p['part_title'])
        if part_title in seen_part_titles:
            print(f'Duplicate part_title found: {part_title}. file_name={file_name}')
            exit(1)
        else:
            seen_part_titles.add(part_title)
        for s in p['sections']:
            print(s['section_title'])

def main():
    required_translations = ['kg', 'bt']
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
            print(f'Error: {file_name}.json was not tested.')
            exit(1)


if __name__ == '__main__':
    main()
