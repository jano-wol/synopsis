import json
import os
import sys

from file_utils import load_json

roman = ['I.', 'II.', 'III.', 'IV.', 'V.', 'VI.', 'VII.', 'VIII.', 'IX.', 'X.', 'XI.', 'XII.', 'XIII.', 'XIV.', 'XV.', 'XVI.',
                 'XVII.', 'XVIII.']

def overwrite_part_titles(json_loaded, part_titles):
    idx = 0
    for p in json_loaded['parts']:
        p['part_title'] = roman[idx] + ' ' + part_titles[roman[idx]]
        idx += 1


def overwrite_section_titles(json_loaded, section_titles):
    idx = 1
    for p in json_loaded['parts']:
        for section in p['sections']:
            r = section['id']
            r += '.'
            section['section_title'] = section_titles[r]
            idx += 1


def main():
    json_folder = sys.argv[1]
    bible = 'ruf'
    language = 'hu'
    ct = load_json('collected_titles.json')
    titles = ct[language]
    part_titles = titles['part_titles']
    section_titles = titles['section_titles']
    p = os.path.join(json_folder, bible + '.json')
    bible_json = load_json(p)
    overwrite_part_titles(bible_json, part_titles)
    overwrite_section_titles(bible_json, section_titles)
    with open(p + '_2', 'w', encoding='utf-8') as f:
        json.dump(bible_json, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    main()
