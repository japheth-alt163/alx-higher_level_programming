#!/usr/bin/python3
"""Defines a JSON-to-object function."""
import json


def from_json_string(my_str):
    """Return the Python object represented by a JSON string.

    Args:
        my_str (str): The JSON string to convert to a Python object.

    Returns:
        any: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
