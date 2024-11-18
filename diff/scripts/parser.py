import json
import os


def parser(file_path):
    extension = os.path.splitext(file_path)[1].lower()
    parser = {
        '.json': json.load,
    }

    if extension not in parser:
        raise ValueError(f"Unsupported file format: {extension}")

    with open(file_path) as file:
        return parser[extension](file)