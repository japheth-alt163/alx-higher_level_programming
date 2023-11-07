#!/usr/bin/python3
"""Defines a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of an object as a string.

    Args:
        my_obj (any): The object to convert to JSON.

    Returns:
        str: The JSON representation of the object as a string.
    """
    return json.dumps(my_obj)
