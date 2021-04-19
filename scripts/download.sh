#!/bin/sh -eu
REPOSITORY_ROOT="$(
    cd "$(dirname "$(dirname "$0")")"
    pwd
)"

RAW_DIR="$REPOSITORY_ROOT"/raw
COMPETISION=imaterialist-fashion-2020-fgvc7
ZIP_FILE="$RAW_DIR"/${COMPETISION}.zip

if [ ! -e "$ZIP_FILE" ]; then
    kaggle competitions download -c $COMPETISION -p "$RAW_DIR"
fi

unzip "$ZIP_FILE" -d "$RAW_DIR"
