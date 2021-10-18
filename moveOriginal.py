from shutil import move
from log import *


def moveOriginal(name, root, base, ext, failed=False):
    """
    Moves image to

    Args:
        name (str): File name
        root (str): Superior path of file; the folder in which the file
                    is stored
        base (str): File name without extension
        ext (str): File extension including a dot as the first character
        failed (bool): Whether to move the file to the failed folder or
                       not
    """

    if not failed:
        move(f"{root}/{name}", (f"{root}/{base}/original{ext}"))
