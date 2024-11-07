import sys

from bible_ref import BibleRef, BibleSec
from file_utils import load_json

evangelists = ['mt', 'mk', 'lk', 'jn']

def verse_to_float(s):
    if s[-1] == 'a':
        return float(s[:-1])
    if s[-1] == 'b':
        return float(s[:-1]) + 0.5
    return float(s)

def get_body_intervals(bible_json) -> list[BibleSec]:
    ret = []
    for evangelist in evangelists:
        for p in bible_json['parts']:
            for section in p['sections']:
                for box in section[evangelist]:
                    if box and box['leading']:
                        chapter_str_1 = box['content'][0]['chapter']
                        verse_str_1 = box['content'][0]['verse']
                        chapter_str_2 = box['content'][-1]['chapter']
                        verse_str_2 = box['content'][-1]['verse']
                        str_1 = f'{evangelist}{chapter_str_1},{verse_str_1}'
                        str_2 = f'{evangelist}{chapter_str_2},{verse_str_2}'
                        start = BibleRef.from_string(str_1)
                        end = BibleRef.from_string(str_2)
                        sec = BibleSec(start, end)
                        sec.fix_close_sec()
                        ret.append(sec)
    return ret


def dc(s):
    s1 = s[2:]
    if '-' in s1:
        result0 = s1.split('-', 1)[0]
        ch1 = float(result0.split(',', 1)[0])
        verse1 = result0.split(',', 1)[1]
        verse1 = verse_to_float(verse1)
        result1 = s1.split('-', 1)[1]
        if ',' in result1:
            ch2 = float(result1.split(',', 1)[0])
            verse2 = result1.split(',', 1)[1]
            verse2 = verse_to_float(verse2)
        else:
            ch2 = ch1
            verse2 = verse_to_float(result1)
    else:
        ch = float(s1.split(',', 1)[0])
        verse = s1.split(',', 1)[1]
        verse = verse_to_float(verse)
        ch1 = ch
        ch2 = ch
        verse1 = verse
        verse2 = verse
    return s[:2], [ch1, verse1], [ch2, verse2]


def main():
    redirect_folder = sys.argv[1]
    translation_folder = sys.argv[2]
    BibleRef.class_init(translation_folder)
    bible_path = translation_folder + '/' + 'kg.json'
    bible_json = load_json(bible_path)
    print(BibleRef.bible_ref_list)
    intervals = get_body_intervals(bible_json)
    to_leading_path = redirect_folder + '/' + 'toLeading.json'
    to_leading_json = load_json(to_leading_path)
    for e in to_leading_json:
        sec = BibleSec.from_closed_string(e)


if __name__ == '__main__':
    main()
