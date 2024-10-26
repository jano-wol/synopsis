import json
import sys


def rewrite(out_bible, titles):
    idx = 0
    for p in out_bible['parts']:
        for s in p['sections']:
            s['section_title'] = titles[idx]
            idx = idx + 1
    if idx != len(titles):
        print(f'No all titles were used. idx={idx}')
        exit(1)



def main():
    json_folder = sys.argv[1]
    titles_path = sys.argv[2]
    override_bible = sys.argv[3]

    titles = []
    with open(titles_path, 'r', encoding='utf-8') as file:
        for line in file:
            l = line.strip()
            titles.append(l)
    override_bible_path = json_folder + override_bible + '.json'
    out_bible_path = json_folder + override_bible + '_override.json'
    with open(override_bible_path, 'r', encoding='utf-8') as f:
        out_bible = json.load(f)
    rewrite(out_bible, titles)
    with open(out_bible_path, 'w', encoding='utf-8') as f:
        json.dump(out_bible, f, ensure_ascii=False, indent=4)



if __name__ == '__main__':
    main()
