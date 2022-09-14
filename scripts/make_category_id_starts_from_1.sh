#!/bin/sh -eu
SCRIPTS_DIR=$(
    cd "$(dirname "$0")"
    pwd
)
PRJ_ROOT=$(dirname "$SCRIPTS_DIR")
RAW_DIR="$PRJ_ROOT"/raw

poetry run python "$PRJ_ROOT"/imaterialist/cli/make_category_id_starts_from_1.py \
    "$RAW_DIR"/instances_attributes_train2020.json \
    "$RAW_DIR"/instances_attributes_train2020_shifted.json
