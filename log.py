from config import debugging
from multitasking import task
from datetime import datetime


@task
def log(error):
    if debugging["enable"]:
        open(str(debugging["logErrors"]["logPath"] + "/logs.log"), "a+").write(
            f"{datetime.now()} :: {error}\n\n"
        )
