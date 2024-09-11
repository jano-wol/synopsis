from bs4 import BeautifulSoup
import json
import os
import sys


def get_change_table_path(components_folder, translation):
    return components_folder + 'TitleChangeTable' + translation + '.vue'


def get_id_and_title(table_element):
    a, b = table_element.split(' ', 1)
    return a, b


def read_overwritten_titles(components_folder, translation):
    path = get_change_table_path(components_folder, translation)
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
            print(f'Change table row contains other than two elements. path={path} row={row}')
            sys.exit(1)
        id1, title1 = get_id_and_title(row[0])
        id2, title2 = get_id_and_title(row[1])
        if id1 != id2:
            print(f'Change table row contains different ids. id1={id1} id2={id2} path={path} row={row}')
            sys.exit(1)
        if title1 == title2:
            print(f'Change table row contains identical titles (superfluous row). title={title1} path={path} row={row}')
            sys.exit(1)
        if id1 in overwritten_titles:
            print(f'Change table contains multiple rows with the same id. id={id1} path={path}')
            sys.exit(1)
        overwritten_titles[id1] = [title1, title2]
    return overwritten_titles


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



def update():
    vue_content = """
<!-- Generated file, update it by calling locally: ./tests/test.sh update -->
<script lang="ts">
import { useSynopsisStore } from "@/stores/SynopsisStore"


export default {
    data() {
        return {
            synopsisStore: useSynopsisStore()
        };
    }
}

</script>

<template>
    <div class="table-responsive">
        <table class="table bg-dark table-sm table-striped table-bordered">
            <thead>
                <tr>
                    <th class="text-nowrap" scope="col">{{ synopsisStore.currentDictionary.sources.originalTitle }}</th>
                    <th class="text-nowrap" scope="col">{{ synopsisStore.currentDictionary.sources.unifiedSZITTitle }}</th>
                </tr>
            </thead>
            <tbody class="table-group-divider">
                <tr>
                    <td class="col-lg-6 align-middle">
                        23. Tartózkodás Kapernaumban
                    </td>
                    <td class="col-lg-6 align-middle">
                        23. Tartózkodás Kafarnaumban
                    </td>
                </tr>
                <!-- More rows... -->
            </tbody>
        </table>
    </div>
</template>
"""


    soup = BeautifulSoup(vue_content, 'html.parser')


    first_row = soup.find('tbody').find_all('tr')[0]
    first_cell = first_row.find_all('td')[0]
    first_cell.string = "23. Modified Location"

    new_row = soup.new_tag('tr')
    new_cell1 = soup.new_tag('td', attrs={"class": "col-lg-6 align-middle"})
    new_cell1.string = "400. New Event"
    new_cell2 = soup.new_tag('td', attrs={"class": "col-lg-6 align-middle"})
    new_cell2.string = "400. New Event Description"
    new_row.append(new_cell1)
    new_row.append(new_cell2)
    soup.find('tbody').append(new_row)

    with open('ModifiedComponent.vue', 'w') as file:
        file.write(soup.prettify())










def main():
    json_folder = sys.argv[1]
    components_folder = sys.argv[2]
    titles_json_file_path = sys.argv[3]
    update_vue = (sys.argv[4] == 'update')
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
            if json_loaded['language'] in titles_json:
                default_titles = titles_json[json_loaded['language']]
                if update_vue:
                    pass
                else:
                    overwritten_titles = read_overwritten_titles(components_folder, translation)
                    check_overwritten(default_titles, overwritten_titles, translation)
                    check_json_titles(json_loaded, default_titles, overwritten_titles, translation)
    if update_vue:
        print(f'Test is failed as update was called')
        sys.exit(1)


if __name__ == "__main__":
    main()
