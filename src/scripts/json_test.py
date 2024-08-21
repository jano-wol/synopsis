import json
import os
import sys

json_folder = sys.argv[1]
json_files_found = False
for file in os.listdir(os.fsencode(json_folder)):
    filename = os.fsdecode(file)
    if filename.endswith(".json"):
        file_to_check = os.path.join(json_folder, filename)
        with open(file_to_check) as f:
            try:
                json_files_found = True
                json_loaded = json.load(f)
            except ValueError as e:
               print(f'Invalid json= {file_to_check}. error={e}')
               sys.exit(1)
if json_files_found is False:
    print(f'No json files were found in folder={json_folder}')
    sys.exit(1)

