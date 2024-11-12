#!/bin/bash
TOOLS_FOLDER=$(dirname "${0}")
WORKSPACE_FOLDER=$(readlink -e "${TOOLS_FOLDER}/../")
TRANSLATION_FOLDER="$WORKSPACE_FOLDER/src/assets/translations/"
python3 $TOOLS_FOLDER/bible_dumper.py $TRANSLATION_FOLDER $BIBLE
