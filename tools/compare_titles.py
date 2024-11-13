import os
import sys

from file_utils import iterate_jsons, load_json
from translation import Translation

def split_part_title(input_string):
    first_dot = input_string.find('.')
    first_space = input_string.find(' ')
    if first_dot == -1:
        split_index = first_space
    elif first_space == -1:
        split_index = first_dot
    else:
        split_index = min(first_dot, first_space)
    if split_index == -1:
        return input_string, ''
    first_part = input_string[:split_index]
    remainder = input_string[split_index + 1:]
    return first_part + '.', remainder[1:]


def main():
    json_folder = sys.argv[1]
    original_titles = load_json('collected_titles.json')
    json_files_found = False
    for json_loaded, json_path in iterate_jsons(json_folder):
        json_files_found = True
        en = json_loaded["language"]
        if en in list(original_titles.keys()):
            translation = Translation(json_loaded)
            with open(json_loaded["translation"] + '_diff_part_titles', 'w', encoding='utf-8') as file:
                file.write('original_part_title <-> current_part_title\n')
                for part_title in translation.part_titles:
                    key, value = split_part_title(part_title)
                    original_title = original_titles[en]['part_titles'][key]
                    if original_title != value:
                        file.write(original_title + ' <-> ' +  value + '\n')
            with open(json_loaded["translation"] + '_diff_section_titles', 'w', encoding='utf-8') as file:
                file.write('original_section_title <-> current_section_title\n')
                for i in range(370):
                    if str(i) in translation.section_titles:
                        value = translation.section_titles[str(i)]
                        original_key = str(i) + '.'
                        original_title = original_titles[en]['section_titles'][original_key]
                        if original_title != value:
                            file.write(original_key  + ' ' + original_title + ' <-> ' + original_key  + ' ' + value + '\n')

    if json_files_found is False:
        print(f'No json files were found in folder={json_folder}')
        sys.exit(1)


if __name__ == '__main__':
    main()
