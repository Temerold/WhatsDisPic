# Import root variable from config.py
import os
import sys

from config import *  # User configuration - Local file (config.py)

# Imports preinstalled packages

# Create required directories

root = './images'

try:
    os.mkdir(root)
except BaseException:
    pass  # Create ./images

try:
    os.mkdir(root + "\\toDo")
except BaseException:
    pass  # Create ./images/toDo

try:
    os.mkdir(root + "\\failed")
except BaseException:
    pass  # Create ./images/failed

try:
    os.mkdir("./models")
except BaseException:
    pass  # Create ./models

# Define clear function


def clear():
    return os.system("cls")  # Define clear() as cls


yes = ["y", "yes"]  # Yes values
no = ["n", "no"]  # No values

try:

    # Looks if all required packages is installed
    import tensorflow
    from colorthief import ColorThief
    from imageai.Prediction import ImagePrediction
    from PIL import Image, ImageColor

    # Init variables
    ask_auto = ""  # Init input boolean

# If not all packages are installed do this
except BaseException:
    clear()  # Clear console before asking for automatic install
    # Ask if user want's automatic packages install
    ask_auto = input("Do you want automatic install of packages? (y/n)")

# Look if Tensorflow is installed
try:
    import tensorflow
except ImportError:
    clear()
    # User want's manual install
    if ask_auto in no:
        sys.exit("""You need tensorflow!
    install it from http://pypi.python.org/pypi/tensorflow
    or run pip install tensorflow.""")

    # User want's automatic install
    elif ask_auto in yes:
        print("Trying to Install required module: tensorflow\n")
        os.system("python -m pip install tensorflow")
        import tensorflow

# Look if ImageAI is installed
try:
    from imageai.Prediction import ImagePrediction
except ImportError:
    clear()
    # User want's manual install
    if ask_auto in no:
        sys.exit("""You need imageai!
    install it from http://pypi.python.org/pypi/imageai
    or run pip install imageai.""")

    # User want's automatic install
    elif ask_auto in yes:
        print("Trying to Install required module: imageai\n")
        os.system("python -m pip install imageai")
        from imageai.Prediction import ImagePrediction

# Look if PIL is installed
try:
    from PIL import Image, ImageColor
except ImportError:
    clear()
    # User want's manual install
    if ask_auto in no:
        sys.exit("""You need pillow!
    install it from http://pypi.python.org/pypi/pillow
    or run pip install pillow""")

    # User want's automatic install
    elif ask_auto in yes:
        print("Trying to Install required module: pillow\n")
        os.system("python -m pip install pillow")
        from PIL import Image, ImageColor

# Look if ColorThief is installed
try:
    from colorthief import ColorThief
except ImportError:
    clear()
    # User want's manual install
    if ask_auto in no:
        sys.exit("""You need colorthief!
    install it from http://pypi.python.org/pypi/colorthief
    or run pip install colorthief.""")

    # User want's automatic install
    elif ask_auto in yes:
        print("Trying to Install required module: colorthief\n")
        os.system("python -m pip install colorthief")
        from colorthief import ColorThief


# root = general[root]
root = './images'
