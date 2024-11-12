import os
import sys

from bible import BibleRef, evangelists
from file_utils import iterate_jsons
from translation import Translation


def get_rw_ref(ref):
    end_str=''
    if ref.x == 1:
        end_str = 'a'
    if ref.x == 2:
        end_str = 'b'
    formatted_chapter = f'{ref.chapter:02}'
    formatted_verse = f'{ref.verse:02}'
    return evangelists[ref.e] + '_' + formatted_chapter + ':' + formatted_verse  + end_str

def construct_line(curr, translation):
    line = get_rw_ref(curr) + ' '
    text = translation.ref_to_text[curr]
    if text is None:
        text = ''
    line += text
    return line

def dump_bible(translation, json_path):
    print(json_path)
    file_name = os.path.splitext(os.path.basename(json_path))[0] + '.txt'
    parts = json_path.split(os.sep)
    assert 'synopsis' in parts
    index = parts.index('synopsis')
    folder_containing_synopsis = os.sep.join(parts[:index])
    file_path = os.path.join(folder_containing_synopsis, file_name)
    with open(file_path, 'w', encoding='utf-8') as file:
        curr = BibleRef.begin()
        while curr != BibleRef.end():
            line = construct_line(curr, translation)
            file.write(line + '\n')
            curr = curr.next()
        cut_verses = translation.get_cut_verses()
        for v in cut_verses:
            a = BibleRef(v.e, v.chapter, v.verse, 1)
            b = BibleRef(v.e, v.chapter, v.verse, 2)
            line = construct_line(a, translation)
            file.write(line + '\n')
            line = construct_line(b, translation)
            file.write(line + '\n')



def main():
    json_folder = sys.argv[1]
    json_files_found = False
    for json_loaded, json_path in iterate_jsons(json_folder):
        json_files_found = True
        translation = Translation(json_loaded)
        dump_bible(translation, json_path)
    if json_files_found is False:
        print(f'No json files were found in folder={json_folder}')
        sys.exit(1)


if __name__ == '__main__':
    main()
