#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """
    Return a list of an object's available attributes.

    Args:
    obj: The object to inspect.

    Returns:
    A list of strings
    """
    return dir(obj)
