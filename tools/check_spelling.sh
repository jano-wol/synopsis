#!/bin/bash
TOOLS_FOLDER=$(dirname "${0}")
WORKSPACE_FOLDER=$(readlink -e "${TOOLS_FOLDER}/../")
TRANSLATION_FOLDER="$WORKSPACE_FOLDER/src/assets/translations/"
BIBLE=$1
LANGUAGE=$(python3 $TOOLS_FOLDER/dump_texts.py $TRANSLATION_FOLDER $BIBLE)
hunspell -d $LANGUAGE -u dump_biblical_text > biblical_text_unknowns
hunspell -d $LANGUAGE -u dump_header > header_unknowns
hunspell -d $LANGUAGE -u dump_part_titles > part_titles_unknowns
hunspell -d $LANGUAGE -u dump_section_titles > section_titles_unknowns
