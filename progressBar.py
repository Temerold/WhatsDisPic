from config import general


def printProgressBar(
    iteration,
    total,
    decimals=0,
    length=10,
    fill="#",
    printEnd="\n",
):

    """
    Calls in a loop to create terminal progress bar.

    Args:
        iteration (int): Current iteration
        total (int): Total iterations (Int)
        prefix (str): Prefix string
        suffix (str): Suffix string
        decimals (int): Positive number of decimals in percent complete
        length (int): Character length of bar
        fill (str): Bar fill character
        printEnd (str): End character (e.g. "\r", "\r\n")
    """

    if general["progressBar"]:
        filledLength = int(length * iteration // total)
        print(
            f"\r|{fill * filledLength + '-' * (length - filledLength)}| "
            + f"{('{0:.' + str(decimals)+ 'f}').format(100 * (iteration / float(total)))}"
            + f"% | {total - iteration}/{total} to go",
            end=printEnd,
        )

        if iteration == total:
            print()
