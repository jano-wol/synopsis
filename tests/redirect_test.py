import sys

from file_utils import load_json

evangelists = ['mt', 'mk', 'lk', 'jn']


class BibleRef:
    bible_refs: dict[str, list['BibleRef']] = {}

    def __init__(self, e: str, c: int, v: int, x: str):
        self.e = e
        self.c = c
        self.v = v
        self.x = x

    def __repr__(self) -> str:
        # This will print a more readable format for debugging
        return f"BibleRef(e='{self.e}', c={self.c}, v={self.v}, x='{self.x}')"

    def __eq__(self, other) -> bool:
        if isinstance(other, BibleRef):
            return (self.e, self.c, self.v, self.x) == (other.e, other.c, other.v, other.x)
        return False

    def custom_leq(self, other) -> bool:
        assert self.e == other.e, "Different evangelists cannot be compered"
        if self.c < other.c :
            return True
        if other.c < self.c:
            return False
        if self.v < other.v :
            return True
        if other.v < self.v:
            return False
        if self.x == 'b' and other.x != 'b':
            return False
        return True


    def custom_lt(self, other) -> bool:
        assert self.e == other.e, "Different evangelists cannot be compered"
        if self.c < other.c :
            return True
        if other.c < self.c:
            return False
        if self.v < other.v :
            return True
        if other.v < self.v:
            return False
        if self.x != 'b' and other.x == 'b':
            return True
        return False

    def custom_eq(self, other) -> bool:
        return self.custom_leq(other) and other.custom_leq(self)

    def next(self) -> 'BibleRef':
        ref_list = BibleRef.bible_refs[self.e]
        idx = ref_list.index(self) + 1
        if self.x == '':
            while ref_list[idx].x != '':
                idx = idx + 1
        return ref_list[idx]

BibleRef.bible_refs = {}


def verse_to_float(s):
    if s[-1] == 'a':
        return float(s[:-1])
    if s[-1] == 'b':
        return float(s[:-1]) + 0.5
    return float(s)


def get_body_intervals(bible_json):
    ret = {}
    for evangelist in evangelists:
        BibleRef.bible_refs[evangelist] = []
        l = []
        for p in bible_json['parts']:
            for section in p['sections']:
                for box in section[evangelist]:
                    if box and box['leading']:
                        l.append([[float(box['content'][0]['chapter']), verse_to_float(box['content'][0]['verse'])],
                                  [float(box['content'][-1]['chapter']), verse_to_float(box['content'][-1]['verse'])]])
                        for v in box['content']:
                            verse_str = v['verse']
                            if verse_str[-1] == 'a':
                                BibleRef.bible_refs[evangelist].append(
                                    BibleRef(evangelist, int(v['chapter']), int(v['verse'][:-1]), ''))
                                BibleRef.bible_refs[evangelist].append(
                                    BibleRef(evangelist, int(v['chapter']), int(v['verse'][:-1]), 'a'))
                            else:
                                if verse_str[-1] == 'b':
                                    BibleRef.bible_refs[evangelist].append(
                                        BibleRef(evangelist, int(v['chapter']), int(v['verse'][:-1]), 'b'))
                                else:
                                    BibleRef.bible_refs[evangelist].append(BibleRef(evangelist, int(v['chapter']), int(v['verse']), ''))


        ret[evangelist] = l
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
    bible_path = translation_folder + '\\' + 'kg.json'
    bible_json = load_json(bible_path)
    intervals = get_body_intervals(bible_json)
    #print(intervals)
    print(f'{BibleRef.bible_refs['mk']}')
    to_leading_path = redirect_folder + '\\' + 'toLeading.json'
    to_leading_json = load_json(to_leading_path)
    for e in to_leading_json:
        evangelist, first, last = dc(e)
        print(f'{evangelist}, {first}, {last}')


if __name__ == '__main__':
    main()
