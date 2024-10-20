import copy
import json
import sys

def parse_line(line):
    evangelists = ['mt', 'mk', 'lk', 'jn']
    space_index = line.find(' ')
    if space_index == -1:
        return None
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
    key_components = [key[:2], key[3:5], key[6:8] + suffix]
    return key_components, line[space_index + 1:]



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
        base_bible = json.load(f)
        out_bible = copy.deepcopy(base_bible)
    with open(out_bible_path, 'w', encoding='utf-8') as f:
        json.dump(out_bible, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()
