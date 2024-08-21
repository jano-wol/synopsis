#!/bin/bash
set -ex
SCRIPT_FOLDER=$(dirname "${0}") 
WORKSPACE_FOLDER=$(readlink -e "${SCRIPT_FOLDER}/../../")
echo "$WORKSPACE_FOLDER"
