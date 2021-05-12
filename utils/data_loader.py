import json
from .dataset import DATA_PATH
from .exceptions import InvalidDatasetName, InvalidDatasetFormat


def load(target: str):

    if not isinstance(target, str):
        raise InvalidDatasetFormat(target)
    if target not in DATA_PATH:
        raise InvalidDatasetName(target)

    with open(DATA_PATH[target], "r", encoding='UTF-8-sig') as f:
        result = json.load(f)

    return result