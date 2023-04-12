#!/usr/bin/python3
"""this import function is used to Defines a JSON-to-object function."""
import json


def from_json_string(my_str):
    """this function Returns  object representation of a JSON string."""
    return json.loads(my_str)
