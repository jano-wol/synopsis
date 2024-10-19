import json
import os
import sys

from file_utils import iterate_jsons


def get_change_table_path(components_folder, translation):
    return components_folder + 'TitleChangeTable' + translation + '.vue'


def get_id_and_title(table_element):
    a, b = table_element.split(' ', 1)
    return a, b


def file_to_string(path):
    with open(path, 'r', encoding='utf-8') as file:
        try:
            return file.read()
        except ValueError as e:
            print(f'Error while reading string from file={path}. error={e}')
            sys.exit(1)


def check_overwritten(default_titles, overwritten_titles, translation):
    if overwritten_titles is None:
        return
    for id1, title_pair in overwritten_titles.items():
        title1, title2 = title_pair
        if id1 not in default_titles:
            print(f'Change table contains unexpected id. id={id1} translation={translation}')
            sys.exit(1)
        default_title = default_titles[id1]
        if default_title != title1:
            print(
                f'Change table mentions wrong default title. id={id1} default_title={default_title} change_table_title={title1} translation={translation}')
            sys.exit(1)


def perform_title_check(id1, json_title, default_titles, overwritten_titles, translation):
    if overwritten_titles is None or id1 not in overwritten_titles:
        if id1 not in default_titles:
            print(f'Translation contains unexpected id. id={id1} translation={translation}')
            sys.exit(1)
        default_title = default_titles[id1]
        if json_title != default_title:
            print(
                f'Translation title is not equal to default title, but the change was not mentioned in change table. id={id1} translation_title={json_title} default_title={default_title} translation={translation}')
            sys.exit(1)
    else:
        overwritten_title = overwritten_titles[id1][1]
        if json_title != overwritten_title:
            print(
                f'Change table title and translation title are not equal. id={id1} change_table_title={overwritten_title} translation_title={json_title} translation={translation}')
            sys.exit(1)


def check_json_titles(json_loaded, default_titles, overwritten_titles, translation):
    for p in json_loaded['parts']:
        part_title = p['part_title']
        id1, json_title = get_id_and_title(part_title)
        perform_title_check(id1, json_title, default_titles, overwritten_titles, translation)
        for s in p['sections']:
            id1 = s['id'] + '.'
            json_title = s['section_title']
            perform_title_check(id1, json_title, default_titles, overwritten_titles, translation)


def update(json_loaded, default_titles, blank_vue, components_folder, translation):
    changes = []
    for p in json_loaded['parts']:
        part_title = p['part_title']
        id1, json_title = get_id_and_title(part_title)
        default_title = default_titles[id1]
        if default_title != json_title:
            changes.append([id1 + ' ' + default_title, id1 + ' ' + json_title])
        for s in p['sections']:
            id1 = s['id'] + '.'
            json_title = s['section_title']
            default_title = default_titles[id1]
            if default_title != json_title:
                changes.append([id1 + ' ' + default_title, id1 + ' ' + json_title])
    if not changes:
        return
    vue_content = file_to_string(blank_vue)


def main():
    json_folder = sys.argv[1]
    for json_loaded, json_path in iterate_jsons(json_folder):
        pass


if __name__ == "__main__":
    main()
