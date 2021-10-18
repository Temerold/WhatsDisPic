from config import dominant
from imageai.Prediction import ImagePrediction
from colorthief import ColorThief
from PIL import Image


def runDominant(name, root, base, ext):
    """
    Prints and creates a local image file with the most used color of an
    image.

    Args:
        name (str): File name
        root (str): Superior path of file; the folder in which the file
                    is stored
        base (str): File name without extension
        ext (str): File extension including a dot as the first character
    """

    if dominant["enable"]:
        dominantColor = ColorThief(f"{root}/{name}").get_color(
            quality=dominant["quality"]
        )  # Get image's dominant color

        width, height = Image.open(f"{root}/{name}").size

        Image.new("RGB", (width, height), (dominantColor)).save(
            f"{root}/{base}/dominantColor{ext}"
        )
        # Save the dominant color image to f"{root}/{base}/dominantColor{ext}"

        print(f"\nDominant Color: {dominantColor}")
