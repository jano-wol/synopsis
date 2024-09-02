#!/bin/bash
set -ex
SCRIPT_FOLDER=$(dirname "${0}") 
WORKSPACE_FOLDER=$(readlink -e "${SCRIPT_FOLDER}/../")
TRANSLATION_FOLDER="$WORKSPACE_FOLDER/src/assets/translations/"
python3 "$SCRIPT_FOLDER"/json_test.py "$TRANSLATION_FOLDER"
echo "All tests passed"