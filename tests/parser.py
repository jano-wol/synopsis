import json
import sys


def parse_line(line):
    evangelists = ['mt', 'mk', 'lk', 'jn']
    space_index = line.find(' ')
    if space_index == -1:
        line = line + ' '
        space_index = line.find(' ')
    key = line[:space_index]
    if len(key) < 8 or len(key) > 9:
        return None
    if key[:2] not in evangelists:
        return None
    if key[2] != '_':
        return None
    if not key[3:5].isdigit():
        return None
    if key[5] != ':':
        return None
    if not key[6:8].isdigit():
        return None
    suffix = ''
    if len(key) == 9:
        if key[8] not in ['a', 'b']:
            return None
        suffix = key[8]
    key_components = [key[:2], str(int(key[3:5])), str(int(key[6:8])) + suffix]
    return key_components, line[space_index + 1:]


def rewrite(input_bible_dict, out_bible, part_titles, section_titles, not_found_keys_fail, unused_keys_warning,
            empty_texts_warning):
    evangelists = ['mt', 'mk', 'lk', 'jn']
    for p in out_bible['parts']:
        part_titles.append(p['part_title'])
        for s in p['sections']:
            section_titles.append(s['section_title'])
            for evangelist in evangelists:
                boxes = s[evangelist]
                if boxes is not None:
                    for box in boxes:
                        if box is not None:
                            for content in box['content']:
                                chapter = content['chapter']
                                verse = content['verse']
                                key = tuple([evangelist, chapter, verse])
                                if key in input_bible_dict:
                                    content['text'] = input_bible_dict[key][0]
                                    if not content['text']:
                                        empty_texts_warning.append(key)
                                    input_bible_dict[key][1] = True
                                else:
                                    not_found_keys_fail.append(key)
    for key, value in input_bible_dict.items():
        if not value[1]:
            unused_keys_warning.append(key)
    not_found_keys_fail[:] = list(set(not_found_keys_fail))
    unused_keys_warning[:] = list(set(unused_keys_warning))
    empty_texts_warning[:] = list(set(empty_texts_warning))


def main():
    json_folder = sys.argv[1]
    input_bible_path = sys.argv[2]
    base_bible = sys.argv[3]
    out_bible_name = sys.argv[4]

    input_bible_dict = {}
    wrong_lines = []
    duplicate_keys = []
    with open(input_bible_path, 'r', encoding='utf-8') as file:
        for line in file:
            l = line.strip()
            if not l:
                continue
            result = parse_line(l)
            if result:
                key, text = result
                key_tuple = tuple(key)
                if key_tuple in input_bible_dict:
                    duplicate_keys.append(l)
                else:
                    input_bible_dict[key_tuple] = [text, False]
            else:
                wrong_lines.append(l)
    if wrong_lines or duplicate_keys:
        if wrong_lines:
            print("\nParse fails:")
            for wrong_line in wrong_lines:
                print(wrong_line)
        if duplicate_keys:
            print("\nDuplicate keys:")
            for duplicate_key in duplicate_keys:
                print(duplicate_key)
        exit(1)
    base_bible_path = json_folder + base_bible + '.json'
    out_bible_path = json_folder + out_bible_name + '.json'
    with open(base_bible_path, 'r', encoding='utf-8') as f:
        out_bible = json.load(f)
    out_bible["translation"] = out_bible_name.upper()

    not_found_keys_fail = []
    unused_keys_warning = []
    empty_texts_warning = []
    part_titles = []
    section_titles = []
    rewrite(input_bible_dict, out_bible, part_titles, section_titles, not_found_keys_fail, unused_keys_warning,
            empty_texts_warning)
    if not_found_keys_fail:
        print(f'Rewrite failed. These keys were not found: {not_found_keys_fail}')
        exit(1)

    with open('part_titles.txt', 'w', encoding='utf-8') as file:
        file.writelines(f'{title}\n' for title in part_titles)
    with open('section_titles.txt', 'w', encoding='utf-8') as file:
        file.writelines(f'{title}\n' for title in section_titles)
    with open(out_bible_path, 'w', encoding='utf-8') as f:
        json.dump(out_bible, f, ensure_ascii=False, indent=4)

    print(f'New bible json was written. path={out_bible_path}')
    print('WARNINGS')
    if empty_texts_warning:
        print(f'The verses corresponding to these keys are empty. keys={empty_texts_warning}')
    if unused_keys_warning:
        print(f'The verse texts for these keys were not used. keys={unused_keys_warning}')
    print('Review and adjust part titles. (A list of them was dumped into part_titles.txt)')
    print('Review and adjust section titles. (A list of them was dumped into section_titles.txt)')
    print(f'Review and adjust out json header. path={out_bible_path}')


if __name__ == '__main__':
    main()
