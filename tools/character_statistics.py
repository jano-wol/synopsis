import os
import sys

from bible import BibleRef
from file_utils import iterate_jsons
from translation import Translation


special_characters = [['\'', '’', '‘', 'ʼ', '′', '‵'], ['-', '–', '—', '‒', '―', '−', '﹣', '⁃']]

def get_texts_exactly_once(t):
    for text in t.iterate_on_part_titles():
        yield text
    for text in t.iterate_on_section_titles():
        yield text
    curr = BibleRef.begin()
    while curr != BibleRef.end():
        text = t.ref_to_text[curr]
        if text:
            yield text
        curr = curr.next()

def main():
    json_folder = sys.argv[1]
    json_files_found = False
    summary = {}
    for json_loaded, json_path in iterate_jsons(json_folder):
        json_files_found = True
        translation = Translation(json_loaded)
        count_list = [[0 for _ in sublist] for sublist in special_characters]
        for text in get_texts_exactly_once(translation):
            for i, sublist in enumerate(special_characters):
                for j, char in enumerate(sublist):
                    count_list[i][j] += text.count(char)
        summary[translation.get_name()] = count_list
    if json_files_found is False:
        print(f'No json files were found in folder={json_folder}')
        sys.exit(1)
    print(special_characters)
    for k, v in summary.items():
        print(f'{k}: {v}')


if __name__ == '__main__':
    main()
