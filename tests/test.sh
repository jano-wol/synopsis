#!/bin/bash
set -ex
SCRIPT_FOLDER=$(dirname "${0}") 
WORKSPACE_FOLDER=$(readlink -e "${SCRIPT_FOLDER}/../")
TRANSLATION_FOLDER="$WORKSPACE_FOLDER/src/assets/translations/"
BLANK_JSON="${SCRIPT_FOLDER}/synopsis_blank.json"
if [[ $1 = "update" ]]; then
    UPDATE="update"
fi	
python3 "$SCRIPT_FOLDER"/json_test.py "$TRANSLATION_FOLDER" "$BLANK_JSON" "$UPDATE"
python3 "$SCRIPT_FOLDER"/consistency_test.py "$TRANSLATION_FOLDER"
python3 "$SCRIPT_FOLDER"/title_test.py "$TRANSLATION_FOLDER"
echo "All tests passed"
