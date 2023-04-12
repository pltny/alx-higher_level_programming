#!/usr/bin/python3
"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """Appends a string.
    Args:
        filename (str): name of the file 
        text (str):string
    Returns:
        The 
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
