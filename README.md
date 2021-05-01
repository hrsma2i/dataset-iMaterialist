# iMaterialist 2020 Dataset Setup Scripts

<!-- TOC -->

- [iMaterialist 2020 Dataset Setup Scripts](#imaterialist-2020-dataset-setup-scripts)
    - [Setup](#setup)
    - [Annotation Format](#annotation-format)
        - [Kaggle Format](#kaggle-format)
        - [COCO Format](#coco-format)
    - [vs ModaNet](#vs-modanet)
    - [vs iMaterialist 2019](#vs-imaterialist-2019)

<!-- /TOC -->

##  Setup

Install Python libraries via Poetry by the following command.

```sh
pip install poetry
poetry install
poetry shell
```

Download images and annotations from Kaggle to `./raw` by the following command.
(Install `kaggel` CLI via pip according to the above instruction that is needed for this script.)

```sh
./scripts/download.sh
```

If you want a tiny dataset for debugging, you can set it up to `./tiny` by the following command. It has the same directory structure as `./raw`.

```sh
./scripts/setup_tiny.sh
```
## Annotation Format

### Kaggle Format

The column `EncodedPixels` in `raw/train.csv` is annotations.
The annotation format is RLE which is **NOT** *COCO* format but an unique format to Kaggle.

You can transform Kaggle RLE annotations to PNGs by the following command. This takes some hours.

```sh
python ./imaterialist/cli/rle2png.py
```

### COCO Format

*COCO* format annotations are also provided as `raw/instances_attributes_{train|val}2020.json`.

**warning**
- Image sizes in the JSON file are different from the actual image sizes. You must resizes images or annotations.
- Two types of annotations are mixed together; `polygons` or `RLE`. c.f., https://github.com/cvdfoundation/fashionpedia/issues/2

## vs ModaNet

ModaNet is another fashion semantic segmentation dataset.

iMaterialist has 27 categories (excluding *garment parts*, *closure*, *decorations*), while [ModaNet has only 13 categories](https://github.com/hrsma2i/modanet#labels).

iMaterialist also has multiple `attributes` annotations per image.


## vs iMaterialist 2019

iMaterialist2020 has more fine-grained attributes (294 kinds) than 2019 (92 kinds).

c.f., https://github.com/visipedia/imat_comp#differences-from-imat-fashion-201920182017
