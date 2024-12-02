import json
import sys

from bible import BibleRef

rename = {'mt': 0,
          'mk': 1,
          'lk': 2,
          'jn': 3}


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

    sub_ref_problems = set()
    for a in start_json:
        assert len(start_json[a]['daily_gospel']) > 0
        dg = start_json[a]['daily_gospel']
        for reading in dg:
            for interval in reading['intervals']:
                if not interval['start']['verse'].isdigit():
                    my_string = interval['start']['verse']
                    rest = my_string[:-1]
                    last_char = my_string[-1]
                    assert rest.isdigit()
                    assert last_char == 'b'
                    sub_ref_problems.add(BibleRef(rename[reading['evangelist']], int(interval['start']['chapter']), int(rest), 1))
                if not interval['end']['verse'].isdigit():
                    my_string = interval['end']['verse']
                    rest = my_string[:-1]
                    last_char = my_string[-1]
                    assert rest.isdigit()
                    assert last_char == 'a'
                    sub_ref_problems.add(BibleRef(rename[reading['evangelist']], int(interval['end']['chapter']), int(rest), 2))
    all_refs = set()
    curr = BibleRef.begin()
    while curr != BibleRef.end():
        all_refs.add(curr)
        curr = curr.next()
    print(len(all_refs))
    for a in start_json:
        assert len(start_json[a]['daily_gospel']) > 0
        dg = start_json[a]['daily_gospel']
        for reading in dg:
            for interval in reading['intervals']:
                assert interval['start']['verse'].isdigit()
                start = BibleRef(rename[reading['evangelist']], int(interval['start']['chapter']),
                             int(interval['start']['verse']), 0)
                if interval['end']['verse'].isdigit():
                    end = BibleRef(rename[reading['evangelist']], int(interval['end']['chapter']),
                               int(interval['end']['verse']), 0)
                else:
                    my_string = interval['end']['verse']
                    rest = my_string[:-1]
                    last_char = my_string[-1]
                    assert rest.isdigit()
                    assert last_char == 'a'
                    x = 1
                    end = BibleRef(rename[reading['evangelist']], int(interval['end']['chapter']), int(rest), x)
                while start <= end:
                    n = BibleRef(start.e, start.chapter, start.verse, 2)
                    if n in sub_ref_problems:
                        if end.get_base_ref() != start:
                            sub_ref_problems.discard(n)
                    all_refs.discard(start)
                    start = start.next()
    print(f'not read because of verse brakes: {sorted(sub_ref_problems)}')
    all_refs_sorted = sorted(all_refs)
    print(f'not read because of missing: {sorted(all_refs_sorted)}')

if __name__ == '__main__':
    main()
