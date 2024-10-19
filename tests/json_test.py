import json
import sys

from file_utils import iterate_jsons


def blank_values(json_element):
    if isinstance(json_element, dict):
        return {k: blank_values(v) for k, v in json_element.items()}
    elif isinstance(json_element, list):
        return [blank_values(item) for item in json_element]
    else:
        return None


def main():
    json_folder = sys.argv[1]
    json_files_found = False
    blank_json_file_path = sys.argv[2]
    with open(blank_json_file_path, 'r', encoding='utf-8') as file:
        blank_json = json.load(file)
    update_blank_json = (sys.argv[3] == 'update')

    for json_loaded, json_path in iterate_jsons(json_folder):
        json_files_found = True
        json_loaded = blank_values(json_loaded)
        if update_blank_json:
            with open(blank_json_file_path, 'w', encoding='utf-8') as file_to_update:
                json.dump(json_loaded, file_to_update, separators=(',', ':'))
            print(f'{blank_json_file_path} was updated. Test is failed as update was called')
            sys.exit(1)
        if json_loaded != blank_json:
            print(f'Invalid json={json_path}. error=Not fitting scheme of blank json.({blank_json_file_path})')
            sys.exit(1)
    if json_files_found is False:
        print(f'No json files were found in folder={json_folder}')
        sys.exit(1)


if __name__ == "__main__":
    main()
