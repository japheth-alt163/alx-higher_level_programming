#!/usr/bin/python3


def inherits_from(obj, a_class):
    """Check if an object is an instance of a class

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare against.

    Returns:
        True if the object is an instance
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
