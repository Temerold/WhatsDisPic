# -*- coding: utf-8 -*-
# WhatsDisPic?


from autoLibInstall import *  # Import dependencies from `deps.py`
from os import mkdir, system, walk, path
from config import general, debugging
from ai import runAI
from dominant import runDominant
from palette import runPalette
from moveOriginal import moveOriginal
from progressBar import *
from log import *
from traceback import format_exc


clear = lambda: system("cls")
clear()
# Clears terminal from warnings and such. Those will be logged anyways
# (if it's toggled on, that is).

totalFileAmount = 0
currentFile = 0
failed = 0

fileTypes = tuple(general["fileTypes"])

for root, dirs, files in walk((general["path"] + "/toDo"), topdown=False):
    for _ in [file for file in files if file.lower().endswith(fileTypes)]:
        totalFileAmount += 1

for root, dirs, files in walk((general["path"] + "/toDo"), topdown=False):
    for name in [file for file in files if file.lower().endswith(fileTypes)]:
        try:
            currentFile += 1

            base, ext = path.splitext(name)

            try:
                mkdir(f"{root}/{base}")
                # Create directory for image f"{root}/{base}"

            except FileExistsError:
                pass
                # Do nothing if the directory already exists. It doesn't
                # need to be logged since it's not an error.

            except Exception as err:
                log(format_exc())

            runAI(name, root, base)
            runDominant(name, root, base, ext)
            runPalette(name, root)
            moveOriginal(name, root, base, ext)

            printProgressBar(currentFile, totalFileAmount)
            print(f"Current File: {name} ({root}{base})\n" + "-" * 100)

        except Exception as err:
            log(format_exc())

            try:
                moveOriginal(name, root, base, ext, True)
            except Exception as err:
                log(format_exc())

            failed += 1

print(f"\nFnished!\nFailed: {failed}\nCompleted: {totalFileAmount - failed}\n")

if failed != 0:
    print(f"Read the logs for more info. ({debugging['logErrors']['logPath']})")
