#!/bin/sh -eux
SCRIPTS_DIR=$(
    cd "$(dirname "$0")"
    pwd
)
PROJECT_ROOT=$(dirname "$SCRIPTS_DIR")
TINY_DIR=$PROJECT_ROOT/tiny
RAW_DIR=$PROJECT_ROOT/raw
N_SAMPLES=52

mkdir -p "$TINY_DIR"

# sample annotations
head -n $N_SAMPLES "$RAW_DIR"/train.csv >"$TINY_DIR"/train.csv

# copy images
mkdir -p "$TINY_DIR"/train
cut -d, -f1 "$TINY_DIR"/train.csv | tail -n +2 | sort | uniq | xargs -I% cp raw/train/% tiny/train

# link to the metadata
ln -snf "$RAW_DIR"/label_descriptions.json "$TINY_DIR"

# RLE annotation -> PNG
python "$PROJECT_ROOT"/imaterialist/cli/rle2png.py \
    --ann-csv "$TINY_DIR/train.csv" \
    --meta-json "$TINY_DIR/label_descriptions.json" \
    --out-dir "$TINY_DIR/ann"
