from load_image import ft_load
import matplotlib.pyplot as plt


def zoom_image(img, x_start=0, x_end=None, y_start=0, y_end=None):
    """
        zoom_image(img, x_start, x_end, y_start, y_end)
        Zoom the image given with the values and open it
    """
    try:
        if x_end is None:
            x_end = img.shape[1]
        if y_end is None:
            y_end = img.shape[0]
        zoomed = img[y_start:y_end, x_start:x_end]
        channels = 1 if len(zoomed.shape) == 2 else zoomed.shape[2]
        print(f"\nNew shape after slicing: {zoomed.shape} \
                or {zoomed.shape[:2]}")
        print(f"Number of channel : {channels}")
        print(zoomed)

        plt.imshow(zoomed, cmap='gray' if len(zoomed.shape) == 2 else None)
        plt.title("Zoomed Image")
        plt.xlabel("Pixel X")
        plt.ylabel("Pixel Y")
        plt.show()

        return zoomed

    except FileNotFoundError:
        print("Erreur : fichier non trouvé :", img)
    except Exception as e:
        print("Une erreur est survenue :", e)


def main():
    print(ft_load.__doc__)
    img = ft_load("animal.jpeg")
    if img is None:
        return
    print(zoom_image.__doc__)
    zoom_image(img, 400, 900, 100, 500)


if __name__ == "__main__":
    main()
