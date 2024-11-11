#!/bin/bash
set -ex
SCRIPT_FOLDER=$(dirname "${0}") 
WORKSPACE_FOLDER=$(readlink -e "${SCRIPT_FOLDER}/../")
TRANSLATION_FOLDER="$WORKSPACE_FOLDER/src/assets/translations/"
REDIRECT_FOLDER="$WORKSPACE_FOLDER/src/assets/redirect/"
BLANK_JSON="${SCRIPT_FOLDER}/synopsis_blank.json"
if [[ $1 = "update" ]]; then
    UPDATE="update"
fi	
python3 "$SCRIPT_FOLDER"/json_test.py "$TRANSLATION_FOLDER" "$BLANK_JSON" "$UPDATE"
python3 "$SCRIPT_FOLDER"/box_test.py "$TRANSLATION_FOLDER"
python3 "$SCRIPT_FOLDER"/redirect_test.py "$TRANSLATION_FOLDER" "$REDIRECT_FOLDER"
python3 "$SCRIPT_FOLDER"/text_consistency_test.py "$TRANSLATION_FOLDER"
python3 "$SCRIPT_FOLDER"/title_test.py "$TRANSLATION_FOLDER"
echo "All tests passed"
