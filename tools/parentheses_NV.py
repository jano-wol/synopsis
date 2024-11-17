import os
import sys

from bible import BibleRef
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

parentheses = []


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
    if counter != 0:
        print(f'TITLE TEST ERROR! {name} {counter} {l}{r}')


def dump_chapter(t, e, chapter):
    curr = BibleRef(e, chapter, 1, 0)
    while curr.e == e and curr.chapter == chapter and curr != BibleRef.end():
        text = t.ref_to_text[curr]
        print(text)
        curr = curr.next()

check_points = [BibleRef(0, 1, 1, 0), BibleRef(1, 1, 1, 0), BibleRef(2, 1, 1, 0),
                BibleRef(2, 14, 1, 0),
                BibleRef(2, 18, 1, 0),
                BibleRef(2, 19, 1, 0),
                BibleRef(2, 19, 11, 0),
                BibleRef(2, 19, 28, 0),
                BibleRef(2, 20, 1, 0),
                BibleRef(2, 20, 5, 0),
                BibleRef(2, 20, 9, 0),
                BibleRef(2, 20, 27, 0),
                BibleRef(2, 22, 1, 0),
                BibleRef(3, 1, 1, 0),
                BibleRef(3, 5, 1, 0),
                BibleRef(3, 6, 1, 0),
                BibleRef(3, 6, 22, 0),
                BibleRef(3, 6, 26, 0),
                BibleRef(3, 6, 59, 0),
                BibleRef(3, 7, 1, 0),
                BibleRef(3, 9, 1, 0),
                BibleRef(3, 9, 11, 0),
                BibleRef(3, 9, 12, 0),
BibleRef(3, 9, 39, 0),
                BibleRef(3, 11, 1, 0),
                BibleRef(3, 13, 1, 0),
                BibleRef(3, 17, 1, 0)]

refresh = [BibleRef(2, 19, 28, 0), BibleRef(2, 20, 9, 0), BibleRef(3, 6, 59, 0)]


def check_parentheses(t):
    name = t.get_name()
    if name != 'NV':
        return
    q = []
    if name in parentheses_map:
        q = parentheses_map[name]
    p = parentheses + q
    for l, r in p:
        test_title(l, r, t)
        counter = 0
        for ref, text in get_texts_exactly_once(t):
            if ref in refresh:
                counter = 0
            if ref in check_points and counter != 0:
                print(f'Checkpoint fail. counter={counter} checkpoint={ref}')
            for c in text:
                if c == l:
                    counter += 1
                if c == r:
                    counter -= 1
                    if counter == -1:
                        print(f'ERROR! {name} {text} {counter} {ref} {l}{r}')
                        counter = 0
        if counter != 0:
            print(f'ERROR! {name} {counter} {l}{r}')


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
