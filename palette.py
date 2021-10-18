from config import palette
from colorthief import ColorThief


def runPalette(name, root):
    """
    Prints the most used colors (in plural) of an image.

    Args:
        name (str): File name
        root (str): Superior path to file; the folder in which the file
                    is stored
    """

    if palette["enable"]:
        print(
            f"""\nImage Palette: {
                ColorThief(f'{root}/{name}').get_palette(
                    color_count=palette['colorCount']
                )
            }"""
        )
