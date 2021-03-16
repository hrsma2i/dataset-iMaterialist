# iMaterialist Dataset Setup Scripts

<!-- TOC -->

- [iMaterialist Dataset Setup Scripts](#imaterialist-dataset-setup-scripts)
    - [Setup](#setup)

<!-- /TOC -->

##  Setup

Download images and annotations from Kaggle to `./raw` by the following command.

```sh
./scripts/download.sh
```

Install Python libraries via Poetry by the following command.

```sh
pip install poetry
poetry install
poetry shell
```

Transform Kaggle RLE annotations to PNGs by the following command. This takes some hours.

```sh
python ./imaterialist/cli/rle2png.py
```

If you want a tiny dataset for debugging, you can set it up to `./tiny` by the following command. It has the same directory structure as `./raw`.

```sh
./scripts/setup_tiny.sh
```
