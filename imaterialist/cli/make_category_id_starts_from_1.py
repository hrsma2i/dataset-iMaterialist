import json
from tqdm import tqdm
from typing import Dict, Any
from pathlib import Path

import pandas as pd
import typer

tqdm.pandas()


def shift(d: Dict[str, Any]) -> Dict[str, Any]:
    df_ann = pd.DataFrame(d["annotations"])
    df_cat = pd.DataFrame(d["categories"])
    df_attr = pd.DataFrame(d["attributes"])

    print("shift categories")
    df_cat["id"] += 1
    df_ann["category_id"] += 1

    print("shift attritbutes")
    df_attr["id"] += 1
    df_ann["attribute_ids"] = df_ann["attribute_ids"].progress_apply(
        lambda attrs: [a + 1 for a in attrs]
    )

    d["annotations"] = df_ann.to_dict(orient="records")
    d["categories"] = df_cat.to_dict(orient="records")
    d["attributes"] = df_attr.to_dict(orient="records")
    return d


def main(
    ann_json: Path,
    out_json: Path,
) -> None:
    """Shift category_id and attribute_id by +1
    to avoid for them to start from 0.
    0 is reserved for the background in many cases.
    The categories in the original COCO dataset also starts from 1.
    """
    print("load json")
    with ann_json.open() as f:
        d = json.load(f)

    d = shift(d)

    print("dump json")
    out_json.parent.mkdir(parents=True, exist_ok=True)
    with out_json.open("w") as f:
        json.dump(d, f, indent=2)


if __name__ == "__main__":
    typer.run(main)
