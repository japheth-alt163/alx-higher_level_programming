#!/usr/bin/python3
"""Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """Convert an object's attributes to a dictionary suitable for JSON serialization.

    Args:
        obj: An instance of a class.

    Returns:
        dict: A dictionary containing the object's attributes.
    """
    return obj.__dict__
