import os
import sys

from bible import BibleRef, evangelists
from file_utils import iterate_jsons
from translation import Translation

parentheses_map = {'KNB': [['‘', '’'], ['»', '«']],
                   'SZIT': [['„', '”']],
                   'RUF': [['„', '”']],
                   'ESV': [['“', '”']],
                   'BT': [['«', '»']],
                   'BJW': [['„', '”']],
                   'NV': [['“', '”']]
                   }

parentheses = [['<', '>'], ['(', ')'], ['{', '}'], ['[', ']']]


def get_titles(t):
    for text in t.iterate_on_part_titles():
        yield text
    for text in t.iterate_on_section_titles():
        yield text

def get_texts_exactly_once(t):
    curr = BibleRef.begin()
    while curr != BibleRef.end():
        text = t.ref_to_text[curr]
        if text:
            yield curr, text
        curr = curr.next()


def test_title(l, r, t):
    name = t.get_name()
    counter = 0
    for text in get_titles(t):
        for c in text:
            if c == l:
                counter += 1
                if c == 2:
                    print(f'{name} {text} {counter} {l}{r} title!!!')
                    counter = 0
            if c == r:
                counter -= 1
                if counter == -1:
                    print(f'{name} {text} {counter} {l}{r} title!!!')
                    counter = 0


def check_parentheses(t):
    name = t.get_name()
    q = []
    if name in parentheses_map:
        q = parentheses_map[name]
    p = parentheses + q
    for l, r in p:
        test_title(l, r, t)
        counter = 0
        old_ref = BibleRef.end()
        for ref, text in get_texts_exactly_once(t):
            if ref.verse == 1 and counter != 0:
                counter = 0
                print(f'{name} {evangelists[old_ref.e]}{old_ref.chapter} contains error.')
            for c in text:
                if c == l:
                    counter += 1
                if c == r:
                    counter -= 1
                    if counter == -1:
                        print(f'{name} {text} {counter} {ref}')
                        counter = 0
            old_ref = ref
        if counter != 0:
                print(f'{name} {evangelists[old_ref.e]}{old_ref.chapter} contains error.')



def main():
    json_folder = sys.argv[1]
    json_files_found = False
    for json_loaded, json_path in iterate_jsons(json_folder):
        json_files_found = True
        translation = Translation(json_loaded)
        check_parentheses(translation)
    if json_files_found is False:
        print(f'No json files were found in folder={json_folder}')
        sys.exit(1)


if __name__ == '__main__':
    main()
