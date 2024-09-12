import json
import os
import sys


def iterate_jsons(json_folder):
    for file in os.listdir(os.fsencode(json_folder)):
        filename = os.fsdecode(file)
        if filename.endswith('.json'):
            json_path = os.path.join(json_folder, filename)
            with open(json_path) as f:
                try:
                    json_loaded = json.load(f)
                    yield json_loaded, json_path
                except ValueError as e:
                    print(f'Invalid json={json_path}. error={e}')
                    sys.exit(1)
