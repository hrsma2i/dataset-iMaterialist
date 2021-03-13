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
