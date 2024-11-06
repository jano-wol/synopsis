import json
import os
import sys


def load_json(json_path):
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f'File not found: {json_path}')
        sys.exit(1)
    except ValueError as e:
        print(f'Invalid JSON in file: {json_path}. Error: {e}')
        sys.exit(1)


def iterate_jsons(json_folder):
    for filename in os.listdir(json_folder):
        if filename.endswith('.json'):
            json_path = os.path.join(json_folder, filename)
            json_loaded = load_json(json_path)
            yield json_loaded, json_path
