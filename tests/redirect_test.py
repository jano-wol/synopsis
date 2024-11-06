import os
import re
import sys

from file_utils import load_json



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
                print(f'KNB={section_title1} <-> SZIT={section_title2}')



def get_body_intervals(bible_json):
    pass


def main():
    redirect_folder = sys.argv[1]
    translation_folder = sys.argv[2]
    bible_json = translation_folder + '\\' + 'kg.json'
    intervals = get_body_intervals(bible_json)

    to_leading_json = redirect_folder + '\\' + 'toLeading.json'

if __name__ == '__main__':
    main()
