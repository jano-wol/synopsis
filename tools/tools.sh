#!/bin/bash
set -ex
TOOLS_FOLDER=$(dirname "${0}")
WORKSPACE_FOLDER=$(readlink -e "${TOOLS_FOLDER}/../")
TRANSLATION_FOLDER="$WORKSPACE_FOLDER/src/assets/translations/"

python3 "$TOOLS_FOLDER"/bible_parser.py "$TRANSLATION_FOLDER" "$TOOLS_FOLDER"/bible_parser_input.txt bt bjw_init
python3 "$TOOLS_FOLDER"/title_compare.py "$TRANSLATION_FOLDER"
python3 "$TOOLS_FOLDER"/title_override.py "$TRANSLATION_FOLDER" "$TOOLS_FOLDER"/title_override_input.txt rsp
python3 "$TOOLS_FOLDER"/dump_texts.py "$TRANSLATION_FOLDER" nv
echo "All tools ran"
