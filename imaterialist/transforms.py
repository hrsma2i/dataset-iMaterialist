import numpy as np


def rle_to_mask(rle: str, height: int, width: int) -> np.ndarray:
    """Decode Kaggle RLE-format annotation to a binary mask for a particular class
    c.f., https://github.com/amirassov/kaggle-imaterialist/blob/master/src/rle.py

    Args:
        rle (str): Kaggle RLE-format annotation string
        height (int): the image's height
        width (int): the image's width

    Returns:
        mask (np.ndarray; {0, 1}^(height, width)):
    """
    rle = np.array([int(x) for x in rle.split(" ")])
    starts, lengths = map(np.asarray, (rle[::2], rle[1::2]))
    starts -= 1
    ends = starts + lengths
    img = np.zeros(height * width, dtype=np.uint8)
    for lo, hi in zip(starts, ends):
        img[lo:hi] = 1
    return img.reshape((width, height)).T
