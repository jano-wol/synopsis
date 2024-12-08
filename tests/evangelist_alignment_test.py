import json
import sys

from bible import evangelists


def main():
    blank_json_file_path = sys.argv[1]
    with open(blank_json_file_path, 'r', encoding='utf-8') as file:
        blank_json = json.load(file)
    for part in blank_json['parts']:
        for section in part['sections']:
            section_id = section['id']
            lengths = {len(section[evangelist]) for evangelist in evangelists}
            assert len(lengths) == 1, \
                f'Evangelist lists have different lengths. section_id={section_id} lengths={lengths}'


if __name__ == '__main__':
    main()
