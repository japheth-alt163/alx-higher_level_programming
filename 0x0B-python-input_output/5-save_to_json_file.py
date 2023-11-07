#!/usr/bin/python3
"""Defines a function to save an object to a JSON file."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a JSON file.

    Args:
        my_obj (any): The Python object to save to the JSON file.
        filename (str): The name of the JSON file to create or overwrite.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
