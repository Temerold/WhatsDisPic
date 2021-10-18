from imageai.Prediction import ImagePrediction
from config import ai


def runAI(name, root, base):
    """
    Prints and writes to file the results of an A.I. engine's
    predictions and prediction probabilities of an image's content.

    Args:
        name (str): File name
        root (str): Superior path to file; the folder in which the file
                    is stored
        base (str): File name without extension
    """

    if ai["enable"]:
        prediction = ImagePrediction()

        try:
            exec(f"prediction.setModelTypeAs{ai['modelType']}()")
        except:
            raise "Unknown A.I. model type."

        prediction.setModelPath(f"./models/{ai['model']}")
        prediction.loadModel()

        predictions, probabilities = prediction.predictImage(
            f"{root}/{name}".replace("/", "/"), result_count=ai["results"]
        )

        # Calculate predictions with their corresponding probabilities

        print("\nPredictions:")

        for eachPrediction, eachProbability in zip(predictions, probabilities):
            print(" " * 4 + f"{eachPrediction}: {round(eachProbability, 1)}%")

            open(f"{root}/{base}/predictions.csv", "a+").write(
                f"{eachPrediction};{eachProbability}%\n"
            )
            # Write each prediction and its probability to
            # f"{root}/{base}/predictions.csv"
