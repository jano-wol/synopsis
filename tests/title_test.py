import json
import os
import sys

tested_translations = ['KG', 'SZIT', 'ESV']
json_folder = sys.argv[1]
titles_json_file_path= sys.argv[2]
with open(titles_json_file_path, 'r') as file:
    titles_json = json.load(file)

for file in os.listdir(os.fsencode(json_folder)):
    filename = os.fsdecode(file)
    if filename.endswith('.json'):
        file_to_check = os.path.join(json_folder, filename)
        with open(file_to_check) as f:
            try:
                json_loaded = json.load(f)
            except ValueError as e:
                print(f'Invalid json= {file_to_check}. error={e}')
                sys.exit(1)
        if json_loaded['translation'] in tested_translations:
            default_titles = titles_json[json_loaded['language']]
