import sys

from file_utils import iterate_jsons
from translation import Translation

forbidden_sub_texts = {'  ', '..', ' …', '… ', ' .', ' ,', ',,'}
exclusions = {'NV_mk5,41': {' .'}}


def get_forbidden_sub_texts_ex(ref, t):
    if ref is None:
        return forbidden_sub_texts
    key = t.get_name() + '_' + str(ref.get_base_ref())
    ex = exclusions.get(key, set())
    return forbidden_sub_texts - ex


def check_forbidden_sub_texts(t):
    for ref, text in t.iterate_on_all_texts():
        if any(subtext in text for subtext in forbidden_sub_texts):
            forbidden_sub_texts_ex = get_forbidden_sub_texts_ex(ref, t)
            assert not any(subtext in text for subtext in
                           forbidden_sub_texts_ex), f'text={text} contains forbidden sub text. Translation={t.get_name()}'


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
