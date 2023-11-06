#!/usr/bin/python3


def add_attribute(obj, attribute, value):
    """Add a new attribute to an object if possible.

    Args:
    obj: The object to which the attribute should be added.
    attribute (str): The name of the attribute to add.
    value: The value to assign to the attribute.

    Raises:
    TypeError: If the attribute cannot be added to the object.
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
