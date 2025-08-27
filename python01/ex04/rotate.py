from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def transpose_image(img, x_start, y_start):
    """
        Takes an image and cut it in a square part and rotate it
    """
    h, w = img.shape[:2]
    squareImg = img[y_start:y_start + 400, x_start:x_start + 400]
    if squareImg is None:
        return

    print(f"The shape of image is: {squareImg.shape} or {squareImg.shape[:2]}")
    print(squareImg)

    # Transposition
    h, w, c = squareImg.shape
    rotatedImg = np.zeros((w, h, c), dtype=squareImg.dtype)
    for i in range(h):
        for j in range(w):
            rotatedImg[j, i] = squareImg[i, j]
    if squareImg is None:
        return

    print(f"New shape after Transpose : {rotatedImg.shape}")
    print(rotatedImg)

    # Affichage
    plt.imshow(rotatedImg, cmap='gray' if len(rotatedImg.shape) == 2 else None)
    plt.title("Transposed Image")
    plt.xlabel("Pixel X")
    plt.ylabel("Pixel Y")
    plt.show()

    return rotatedImg


def main():
    print(ft_load.__doc__)
    img = ft_load("animal.jpeg")
    if img is None:
        return
    print(transpose_image.__doc__)
    transpose_image(img, 400, 100)


if __name__ == "__main__":
    main()
