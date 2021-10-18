from os import mkdir, system
from log import *

yes = ["y", "yes", "1"]  # Yes values
no = ["n", "no", "0"]  # No values

packages = [
    ["tf-nightly", "http://pypi.python.org/pypi/tf-nightly"],
    ["tensorflow", "http://pypi.python.org/pypi/tensorflow"],
    ["ImageAI", "http://pypi.python.org/pypi/imageai"],
    ["Pillow", "http://pypi.python.org/pypi/pillow"],
    ["ColorThief", "http://pypi.python.org/pypi/colorthief"],
    ["PyYAMl", "https://pypi.org/project/pyyaml"],
    ["MultiTasking", "https://pypi.org/project/multitasking"],
]

try:  # Check if all required packages are installed
    import tensorflow
    import colorthief
    import imageai.Prediction
    import PIL
    import yaml
    import multitasking

except ImportError:  # If not, ask to install them automatically
    system("cls")

    askForAutomaticInstall = None

    while askForAutomaticInstall not in yes and askForAutomaticInstall not in no:
        askForAutomaticInstall = input(
            "Do you want an automatic install of the packages? (y/n): "
        )

        for lib in packages:
            if askForAutomaticInstall in no:
                missingLibs = "Missing packages: "

                for lib in packages:
                    try:
                        if lib[0] == "Pillow":
                            lib[0] = "PIL"
                        elif lib[0] == "PyYaml":
                            lib[0] = "yaml"
                        elif lib[0] == "tf-nightly":
                            lib[0] = "tensorflow"
                        # Some libraries are imported using different
                        # names than the one's they use according to
                        # their pip pages.

                        exec(f"import {lib[0]}")

                    except ImportError:
                        missingLibs += f"\n{lib[0]}: {lib[1]}"
                    except Exception as error:
                        raise error

                raise ImportError(missingLibs)

            else:
                system(f"python -m pip install {lib[0]}")
                print("hej")

        if askForAutomaticInstall is None:
            print('You can only answer using "y" or "n"!')

except Exception as err:
    log(err)


from config import *


root = general["path"]


# Create required directories
dirsToCreate = [root, (root + "/toDo"), (root + "/failed"), "./models", "./logs"]

for dir in dirsToCreate:
    try:
        mkdir(dir)
    except:
        pass
        # Do nothing if the directory already exists. It doesn't need to
        # be logged since it's not an error, just a check.
