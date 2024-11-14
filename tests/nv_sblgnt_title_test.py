import os
import sys

from file_utils import load_json
from translation import Translation


def main():
    json_folder = sys.argv[1]
    json_path_nv = os.path.join(json_folder, 'nv.json')
    json_path_sblgnt = os.path.join(json_folder, 'sblgnt.json')
    json_nv = load_json(json_path_nv)
    json_sblgnt = load_json(json_path_sblgnt)
    nv = Translation(json_nv)
    sblgnt = Translation(json_sblgnt)
    for title_nv, title_sblgnt in zip(nv.iterate_on_part_titles(), sblgnt.iterate_on_part_titles()):
        assert title_nv == title_sblgnt, f'nv and sblgnt part title misalignment. title_nv={title_nv} title_sblgnt={title_sblgnt}'
    for title_nv, title_sblgnt in zip(nv.iterate_on_section_titles(), sblgnt.iterate_on_section_titles()):
        assert title_nv == title_sblgnt, f'nv and sblgnt section title misalignment. title_nv={title_nv} title_sblgnt={title_sblgnt}'


if __name__ == '__main__':
    main()
