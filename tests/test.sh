#!/bin/bash
set -ex
SCRIPT_FOLDER=$(dirname "${0}") 
WORKSPACE_FOLDER=$(readlink -e "${SCRIPT_FOLDER}/../")
TRANSLATION_FOLDER="$WORKSPACE_FOLDER/src/assets/translations/"
BLANK_JSON="${SCRIPT_FOLDER}/synopsis_blank.json"
python3 "$SCRIPT_FOLDER"/json_test.py "$TRANSLATION_FOLDER" "$BLANK_JSON"
echo "All tests passed"