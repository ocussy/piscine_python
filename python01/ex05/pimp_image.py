import numpy as np
import matplotlib.pyplot as plt


def show_image(array, title="Image"):
    channels = 1 if len(array.shape) == 2 else array.shape[2]
    plt.imshow(array, cmap='gray' if channels == 1 else None)
    plt.title(title)
    plt.xlabel("Pixel X")
    plt.ylabel("Pixel Y")
    plt.show()


def ft_invert(array) -> np.ndarray:
    """
            ft_invert(array)
        Invert the RGB of the colors
        new value = 255 - old value
    """
    h, w = array.shape[:2]
    c = array.shape[2]
    result = np.zeros((h, w, c), dtype=array.dtype)
    for i in range(h):
        for j in range(w):
            for k in range(c):
                result[i, j, k] = 255 - array[i, j, k]
    show_image(result)
    return result


def ft_red(array) -> np.ndarray:
    """
            ft_red(array)
        Make a red filter using = and *
        We only keep the first value of the RGB code
        R = R
        G = G * 0
        B = B * 0
    """
    h, w, c = array.shape
    result = np.zeros((h, w, c), dtype=array.dtype)
    for i in range(h):
        for j in range(w):
            r = array[i, j, 0]
            g = array[i, j, 1] * 0
            b = array[i, j, 2] * 0
            result[i, j, 0] = r
            result[i, j, 1] = g
            result[i, j, 2] = b
    show_image(result)
    return result


def ft_green(array) -> np.ndarray:
    """
            ft_green(array)
        Make a green filter using = and -
        We only keep the second value of the RGB code
        G = G
        R - R = 0
        B - B = 0
    """
    h, w, c = array.shape
    result = np.zeros((h, w, c), dtype=array.dtype)
    for i in range(h):
        for j in range(w):
            r = array[i, j, 0] - array[i, j, 0]
            g = array[i, j, 1]
            b = array[i, j, 2] - array[i, j, 2]
            result[i, j, 0] = r
            result[i, j, 1] = g
            result[i, j, 2] = b
    show_image(result)
    return result


def ft_blue(array) -> np.ndarray:
    """
            ft_blue(array)
        Make a blue filter using =
        We only keep the third value of the RGB code
        B = B
        R = 0
        G = 0
    """
    h, w, c = array.shape
    result = np.zeros((h, w, c), dtype=array.dtype)
    for i in range(h):
        for j in range(w):
            result[i, j, 0] = 0
            result[i, j, 1] = 0
            result[i, j, 2] = array[i, j, 2]
    show_image(result)
    return result


def ft_grey(array) -> np.ndarray:
    """
            ft_grey(array)
        Make a grey filter using = and /
        Grey = (R + G + B)/3
        (R,G,B)→(Grey,Grey,Grey)
    """
    h, w, c = array.shape
    result = np.zeros((h, w, c), dtype=array.dtype)
    for i in range(h):
        for j in range(w):
            r, g, b = array[i, j]
            grey = (int(r) + int(g) + int(b)) // 3
            result[i, j] = (grey, grey, grey)
    show_image(result)
    return result
