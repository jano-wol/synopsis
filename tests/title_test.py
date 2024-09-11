import json
import os
import sys
from bs4 import BeautifulSoup

tested_translations = ['KG', 'SZIT', 'ESV']
json_folder = sys.argv[1]
components_folder = sys.argv[2]
titles_json_file_path = sys.argv[3]
with open(titles_json_file_path, 'r') as file:
    titles_json = json.load(file)


def read_overwritten_titles(translation_str):
    ret = None
    path = components_folder + 'TitleChangeTable' + translation_str + '.vue'
    if os.path.isfile(path) is False:
        return ret
    with open(path, 'r', encoding='utf-8') as filee:
        try:
            vue_content = filee.read()
        except ValueError as er:
            print(f'Error while reading string from file={path}. error={er}')
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
    for row in table_data:
        print(row)


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
            overwritten_titles = read_overwritten_titles(translation)
