class InvalidDataset(Exception):

    def __init__(self, param):
        self.param = param


class InvalidDatasetFormat(InvalidDataset):

    def __str__(self):
        return f"{self.param}은 str type이 아닙니다."


class InvalidDatasetName(InvalidDataset):

    def __str__(self):
        return f"해당 이름의 Dataset은 존재하지 않습니다: {self.name}"