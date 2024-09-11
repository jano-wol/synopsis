import json
import os
import sys


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
    with open(blank_json_file_path, 'r') as file:
        blank_json = json.load(file)
    update_blank_json = (sys.argv[3] == 'update')

    for file in os.listdir(os.fsencode(json_folder)):
        filename = os.fsdecode(file)
        if filename.endswith('.json'):
            file_to_check = os.path.join(json_folder, filename)
            with open(file_to_check) as f:
                try:
                    json_files_found = True
                    json_loaded = json.load(f)
                except ValueError as e:
                    print(f'Invalid json= {file_to_check}. error={e}')
                    sys.exit(1)
                json_loaded = blank_values(json_loaded)
                if update_blank_json:
                    with open(blank_json_file_path, 'w') as file_to_update:
                        json.dump(json_loaded, file_to_update, separators=(',', ':'))
                    sys.exit(0)
                if json_loaded != blank_json:
                    print(
                        f'Invalid json= {file_to_check}. error=Not fitting scheme of blank json.({blank_json_file_path})')
                    sys.exit(1)
    if json_files_found is False:
        print(f'No json files were found in folder={json_folder}')
        sys.exit(1)


if __name__ == "__main__":
    main()
