#!/bin/bash
TOOLS_FOLDER=$(dirname "${0}")
WORKSPACE_FOLDER=$(readlink -e "${TOOLS_FOLDER}/../")
DATA_FOLDER="$WORKSPACE_FOLDER/data/"
START_JSON_NAME="daily_gospel_general.json"
python3 $TOOLS_FOLDER/daily_gospel_formatter.py $DATA_FOLDER$START_JSON_NAME
