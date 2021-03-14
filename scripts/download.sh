#!/bin/sh -eu
REPOSITORY_ROOT="$(
    cd "$(dirname "$(dirname "$0")")"
    pwd
)"

RAW_DIR="$REPOSITORY_ROOT"/raw
ZIP_FILENAME=imaterialist-fashion-2019-FGVC6.zip
ZIP_FILE="$RAW_DIR"/$ZIP_FILENAME

if [ ! -e "$ZIP_FILE" ]; then
    kaggle competitions download -c imaterialist-fashion-2019-FGVC6 -p "$RAW_DIR"
fi

unzip "$ZIP_FILE" -d "$RAW_DIR"
