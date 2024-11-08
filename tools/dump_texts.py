import json
import os
import sys

from file_utils import load_json

def find_values_by_key(data, target_key):
    if isinstance(data, dict):
        for key, value in data.items():
            if key == target_key:
                yield value
            else:
                yield from find_values_by_key(value, target_key)
    elif isinstance(data, list):
        for item in data:
            yield from find_values_by_key(item, target_key)

def dump_header(bible_json):
    with open("dump_header", 'w', encoding='utf-8') as f:
        for key, value in bible_json.items():
            if key == "parts":
                break
            if key == "evangelists":
                for _, value_1 in value.items():
                    f.write(value_1 + '\n')
            else:
                f.write(value + '\n')

def dump_part_titles(bible_json):
    with open("dump_part_titles", 'w', encoding='utf-8') as f:
        for value in find_values_by_key(bible_json, 'part_title'):
            if isinstance(value, str):
                f.write(value + '\n')

def dump_section_titles(bible_json):
    with open("dump_section_titles", 'w', encoding='utf-8') as f:
        for value in find_values_by_key(bible_json, 'section_title'):
            if isinstance(value, str):
                f.write(value + '\n')

def dump_biblical_text(bible_json):
    with open("dump_biblical_text", 'w', encoding='utf-8') as f:
        for value in find_values_by_key(bible_json, 'text'):
            if isinstance(value, str):
                f.write(value + '\n')


def main():
    json_folder = sys.argv[1]
    bible = sys.argv[2]
    p = os.path.join(json_folder, bible + '.json')
    bible_json = load_json(p)
    dump_header(bible_json)
    dump_part_titles(bible_json)
    dump_section_titles(bible_json)
    dump_biblical_text(bible_json)

if __name__ == '__main__':
    main()
