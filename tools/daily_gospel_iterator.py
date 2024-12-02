import json
import sys


def main():
    start_json_path = sys.argv[1]
    with open(start_json_path, 'r', encoding='utf-8') as f:
        start_json = json.load(f)

    colours = set()
    for a in start_json:
        if start_json[a]['colour'] is None:
            continue
        assert len(start_json[a]['colour']) < 3
        for c in start_json[a]['colour']:
            colours.add(c)
    print(colours)

    broken_verses = set()
    for a in start_json:
        assert len(start_json[a]['daily_gospel']) > 0
        dg = start_json[a]['daily_gospel']
        for reading in dg:
            for interval in reading['intervals']:
                if not interval['start']['verse'].isdigit():
                    broken_verses.add(reading['evangelist'] + '_' + str(interval['end']['chapter']) + '_' + interval['start']['verse'])
                if not interval['end']['verse'].isdigit():
                    broken_verses.add(reading['evangelist'] + '_' + str(interval['end']['chapter']) + '_' + interval['end']['verse'])
    print(broken_verses)

if __name__ == '__main__':
    main()
