import json
import sys

rename = { 'Matthew' : 'mt',
           'Mark'    : 'mk',
           'Luke'    : 'lk',
           'John'    : 'jn' }


def decode(daily_str):
    ret = {}
    evangelist = daily_str.split(' ')[0]
    rest_str = daily_str.split(' ')[1]
    ret['evangelist'] = rename[evangelist]
    return ret


def main():
    start_json_path = sys.argv[1]
    with open(start_json_path, 'r', encoding='utf-8') as f:
        start_json = json.load(f)

    colour_map = {}
    for key in start_json.keys():
        colour_str = start_json[key]['colour']
        color_list = colour_str.split(" or ") if colour_str else None
        colour_map[key] = color_list

    daily_gospel_map = {}
    for key in start_json.keys():
        daily_gospel_map[key] = []
        for daily_str in start_json[key]['daily_gospel']:
            daily_gospel_map[key].append(decode(daily_str))

    combined_map = {
        key: {
            "colour": colour_map.get(key, None),
            "daily_gospel": daily_gospel_map.get(key, [])
        }
        for key in daily_gospel_map.keys() | colour_map.keys()
    }
    combined_map_sorted = {key: combined_map[key] for key in sorted(combined_map)}

    output_file = start_json_path + '_2'
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(combined_map_sorted, file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()
