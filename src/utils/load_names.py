import json


def load_names(file_path: str) -> list:
    with open(file_path, "r") as file:
        return json.load(file)["names"]
