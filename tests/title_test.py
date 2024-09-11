import json
import os
import sys
from bs4 import BeautifulSoup

tested_translations = ['KG', 'SZIT', 'ESV']


def getKeyAndTitle(table_element):
    a, b = table_element.split(' ', 1)
    return a, b


def read_overwritten_titles(translation, components_folder):
    path = components_folder + 'TitleChangeTable' + translation + '.vue'
    if os.path.isfile(path) is False:
        return None
    with open(path, 'r', encoding='utf-8') as file:
        try:
            vue_content = file.read()
        except ValueError as e:
            print(f'Error while reading string from file={path}. error={e}')
            sys.exit(1)

    soup = BeautifulSoup(vue_content, 'html.parser')
    template_content = soup.find('template')
    table = template_content.find('table')
    rows = table.find_all('tr')
    table_data = []
    for row in rows:
        cols = row.find_all('td')
        if cols:
            cols = [col.string.strip() for col in cols]
            table_data.append(cols)
    overwritten_titles = {}
    for row in table_data:
        if len(row) != 2:
            print(f'Table row contains other than two elements. path={path} row={row}')
            sys.exit(1)
        id1, title1 = getKeyAndTitle(row[0])
        id2, title2 = getKeyAndTitle(row[1])
        if id1 != id2:
            print(f'Table row contains different ids. id1={id1} id2={id2} path={path} row={row}')
            sys.exit(1)
        if title1 == title2:
            print(f'Table row contains identical titles (superfluous row). title={title1} path={path} row={row}')
            sys.exit(1)
        if id1 in overwritten_titles:
            print(f'Same Id is presented in multiple rows. id={id1} path={path}')
            sys.exit(1)
        overwritten_titles[id1] = [title1, title2]
    return overwritten_titles

def main():
    json_folder = sys.argv[1]
    components_folder = sys.argv[2]
    titles_json_file_path = sys.argv[3]
    with open(titles_json_file_path, 'r') as file:
        titles_json = json.load(file)
    for file in os.listdir(os.fsencode(json_folder)):
        filename = os.fsdecode(file)
        if filename.endswith('.json'):
            file_to_check = os.path.join(json_folder, filename)
            with open(file_to_check) as f:
                try:
                    json_loaded = json.load(f)
                except ValueError as e:
                    print(f'Invalid json= {file_to_check}. error={e}')
                    sys.exit(1)
            translation = json_loaded['translation']
            if translation in tested_translations:
                default_titles = titles_json[json_loaded['language']]
                overwritten_titles = read_overwritten_titles(translation, components_folder)
                x = 0


if __name__ == "__main__":
    main()
