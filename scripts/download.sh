#!/bin/sh -eu
REPOSITORY_ROOT="$(
    cd "$(dirname "$(dirname "$0")")"
    pwd
)"
kaggle competitions download -c imaterialist-fashion-2019-FGVC6 -p "$REPOSITORY_ROOT"/raw
