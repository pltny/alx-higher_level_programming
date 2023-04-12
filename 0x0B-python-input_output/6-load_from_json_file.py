#!/usr/bin/python3
"""iThis function Defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """This part is used to Create a Python object from a JSON file."""
    with open(filename) as f:
        return json.load(f)
