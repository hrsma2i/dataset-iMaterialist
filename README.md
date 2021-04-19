# iMaterialist Dataset Setup Scripts

<!-- TOC -->

- [iMaterialist Dataset Setup Scripts](#imaterialist-dataset-setup-scripts)
    - [Setup](#setup)

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


Transform Kaggle RLE annotations to PNGs by the following command. This takes some hours.

```sh
python ./imaterialist/cli/rle2png.py
```

If you want a tiny dataset for debugging, you can set it up to `./tiny` by the following command. It has the same directory structure as `./raw`.

```sh
./scripts/setup_tiny.sh
```
