import json
from pathlib import Path
from typing import List

import numpy as np
import pandas as pd
import typer
from segmentation.transforms import masks_to_segmap, segmap_to_pil

from imaterialist.transforms import rle_to_mask


PROJECT_ROOT = Path(__file__).parents[2]


def main():
    typer.run(rle2png)


def rle2png(
    ann_csv: Path = typer.Option(
        PROJECT_ROOT / "raw/train.csv",
        help="an annotaion CSV file",
    ),
    meta_json: Path = typer.Option(
        PROJECT_ROOT / "raw/label_descriptions.json",
        help="a metadata JSON file",
    ),
    out_dir: Path = typer.Option(
        PROJECT_ROOT / "raw/ann",
        help="output PNG annotations directory",
    ),
):
    with open(meta_json) as f:
        meta = json.load(f)
    df_ctg = pd.DataFrame(meta["categories"]).set_index("id")
    # Remove some categories
    df_ctg = df_ctg[
        ~df_ctg["supercategory"].isin(["garment parts", "closures", "decorations"])
    ]

    df = pd.read_csv(ann_csv)
    df["category_id"] = df["ClassId"].apply(lambda c: c.split("_")[0]).astype("int32")
    df = df[df["category_id"].isin(df_ctg.index)]
    df = df.groupby("ImageId").agg(list).reset_index()

    out_dir.mkdir(parents=True, exist_ok=True)
    counter = Counter(len(df))
    df.apply(
        lambda row: save_png_from_rle(
            image_id=row["ImageId"],
            rles=row["EncodedPixels"],
            heights=row["Height"],
            widths=row["Width"],
            category_ids=row["category_id"],
            all_category_ids=df_ctg.index,
            out_dir=out_dir,
            counter=counter,
        ),
        axis=1,
    )


class Counter:
    def __init__(self, total):
        self.i = 0
        self.total = total

    @property
    def per(self):
        return int(100 * self.i / self.total)


def save_png_from_rle(
    image_id: str,
    rles: List[str],
    heights: List[int],
    widths: List[int],
    category_ids: List[int],
    all_category_ids: np.ndarray,
    out_dir: Path,
    counter: Counter,
):
    masks = np.stack(
        [rle_to_mask(r, h, w) for r, h, w in zip(rles, heights, widths)],
        axis=-1,
    )
    # masks: (height, width, #rles)

    segmap = masks_to_segmap(masks, np.array(category_ids))
    # segmap: (height, width)

    png = segmap_to_pil(segmap, all_category_ids)
    png.save(out_dir / image_id.replace("jpg", "png"))

    counter.i += 1
    print(f"{counter.per}[%]={counter.i}/{counter.total}")


if __name__ == "__main__":
    main()
