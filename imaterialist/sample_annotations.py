import json
from pathlib import Path

import typer
import pandas as pd


def main():
    typer.run(sample)


def sample(ann_json: Path, out_json: Path, num_samples: int = 100):
    with ann_json.open() as f:
        d = json.load(f)

    df_img = pd.DataFrame(d["images"]).sample(num_samples, random_state=12345)

    df_ann = pd.DataFrame(d["annotations"])
    df_ann = df_ann[df_ann["image_id"].isin(df_img["id"])]

    d["images"] = df_img.to_dict(orient="records")
    d["annotations"] = df_ann.to_dict(orient="records")

    out_json.parent.mkdir(parents=True, exist_ok=True)
    with out_json.open("w") as f:
        json.dump(d, f, indent=2)


if __name__ == "__main__":
    main()
