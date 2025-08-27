from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
        ft_load(path)
        Open an image with its path and get its size
        and its pixels content in RGB format
    """
    try:
        im = Image.open(path)
        arr = np.array(im)
        print("Before zoom :")
        print("The shape of image is :", arr.shape)
        print(arr)
        return arr
    except Exception as e:
        print("Error :", e)
