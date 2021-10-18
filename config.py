from os import system


try:
    import yaml
except ImportError:
    system("python -m pip install pyyaml")
except Exception as err:
    print(err)

import yaml

data = yaml.load(open("./config.yaml", "r"), yaml.SafeLoader)

general = data["general"]
ai = data["ai"]
dominant = data["dominant"]
palette = data["palette"]
debugging = data["debugging"]
