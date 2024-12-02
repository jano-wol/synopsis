import json
import sys


def main():
    start_json_path = sys.argv[1]
    with open(start_json_path, 'r', encoding='utf-8') as f:
        start_json = json.load(f)
    print(start_json)


if __name__ == '__main__':
    main()
