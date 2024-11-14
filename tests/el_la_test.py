import os
import sys

from file_utils import load_json
from translation import Translation

def main():
    json_folder = sys.argv[1]
    json_path_el = os.path.join(json_folder, 'el.json')
    json_path_la = os.path.join(json_folder, 'la.json')
    json_el = load_json(json_path_el)
    json_la = load_json(json_path_la)
    el = Translation(load_json(json_el))
    la = Translation(load_json(json_la))
    for title_el, title_la in zip (el.iterate_on_part_titles(), la.iterate_on_part_titles()):
        assert title_el == title_la, f'el and la part title misalignment. title_el={title_el} title_la={title_la}'
    for title_el, title_la in zip (el.iterate_on_section_titles(), la.iterate_on_section_titles()):
        assert title_el == title_la, f'el and la section title misalignment. title_el={title_el} title_la={title_la}'

if __name__ == '__main__':
    main()
