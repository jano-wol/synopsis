import copy
import json
import os
import sys


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
    json_folder = sys.argv[1]
    input_bible_path = sys.argv[2]
    base_bible = sys.argv[3]
    out_bible_name = sys.argv[4]

    input_bible_dict = {}
    with open(input_bible_path, 'r', encoding='utf-8') as file:
        for line in file:
            l = line.strip()

    base_bible_path = json_folder + base_bible + '.json'
    out_bible_path = json_folder + out_bible_name + '.json'
    with open(base_bible_path, 'r', encoding='utf-8') as f:
        base_bible = json.load(f)
        out_bible = copy.deepcopy(base_bible)

    with open(out_bible_path, 'w', encoding='utf-8') as f:
        json.dump(out_bible, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()
