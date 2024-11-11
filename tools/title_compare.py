import os
import sys

from file_utils import load_json

checked_translations = ['knb', 'szit']


def compare_part_titles(t1, t2):
    for part1, part2 in zip(t1['parts'], t2['parts']):
        part_title1 = part1['part_title']
        part_title2 = part2['part_title']
        if part_title1 != part_title2:
            print(f'KNB={part_title1} <-> SZIT={part_title2}')


def compare_section_titles(t1, t2):
    for part1, part2 in zip(t1['parts'], t2['parts']):
        sections1 = part1['sections']
        sections2 = part2['sections']
        for section1, section2 in zip(sections1, sections2):
            section_title1 = section1['section_title']
            section_title2 = section2['section_title']
            if section_title1 != section_title2:
                print(
                    f'{checked_translations[0].upper()}={section_title1} <-> {checked_translations[1].upper()}={section_title2}')


def compare_translations(t1, t2):
    compare_part_titles(t1, t2)
    compare_section_titles(t1, t2)


def main():
    json_folder = sys.argv[1]
    p1 = os.path.join(json_folder, checked_translations[0] + '.json')
    p2 = os.path.join(json_folder, checked_translations[1] + '.json')
    t1 = load_json(p1)
    t2 = load_json(p2)
    compare_translations(t1, t2)


if __name__ == '__main__':
    main()
