#!/usr/bin/python3
"""Defines a class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an in

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare against.

    Returns:
        True if obj is an instance of,
    """
    return isinstance(obj, a_class)
