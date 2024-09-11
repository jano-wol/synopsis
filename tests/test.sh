#!/bin/bash
set -ex
SCRIPT_FOLDER=$(dirname "${0}") 
WORKSPACE_FOLDER=$(readlink -e "${SCRIPT_FOLDER}/../")
TRANSLATION_FOLDER="$WORKSPACE_FOLDER/src/assets/translations/"
COMPONENTS_FOLDER="$WORKSPACE_FOLDER/src/components/"
BLANK_JSON="${SCRIPT_FOLDER}/synopsis_blank.json"
TITLES_JSON="${SCRIPT_FOLDER}/synopsis_titles.json"
BLANK_VUE="${SCRIPT_FOLDER}/blank.vue"
if [[ $1 = "update" ]]; then
    UPDATE="update"
fi	
python3 "$SCRIPT_FOLDER"/json_test.py "$TRANSLATION_FOLDER" "$BLANK_JSON" "$UPDATE"
python3 "$SCRIPT_FOLDER"/title_test.py "$TRANSLATION_FOLDER" "$COMPONENTS_FOLDER" "$TITLES_JSON" "$BLANK_VUE" "$UPDATE"
echo "All tests passed"
