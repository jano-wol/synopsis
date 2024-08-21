import json
import os
import sys

json_folder = sys.argv[1]
for file in os.listdir(os.fsencode(json_folder)):
    filename = os.fsdecode(file)
    if filename.endswith(".json"):
        file_to_check = os.path.join(json_folder, filename)
        with open(file_to_check) as f:
            try:
                json.load(f)
            except ValueError as e:
               print(f'Invalid json= {file_to_check}. error={e}')
               sys.exit(1)
