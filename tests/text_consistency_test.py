import sys

from file_utils import iterate_jsons
from translation import Translation

forbidden_sub_texts = ['  ', '..', ' …', '… ']

def check_forbidden_sub_texts(t):
    for text in t.iterate_on_all_texts():
        assert not any(subtext in text for subtext in forbidden_sub_texts), f'text={text} contains forbidden sub text. Translation={t.get_name()}'



def main():
    json_folder = sys.argv[1]
    json_files_found = False
    for json_loaded, json_path in iterate_jsons(json_folder):
        json_files_found = True
        t = Translation(json_loaded)
        check_forbidden_sub_texts(t)
    if json_files_found is False:
        print(f'No json files were found in folder={json_folder}')
        sys.exit(1)


if __name__ == '__main__':
    main()
