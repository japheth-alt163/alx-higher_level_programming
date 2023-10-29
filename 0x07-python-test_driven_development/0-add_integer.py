#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): first integer or float.
        b (int or float, optional): second integer or float. Defaults to 98.

    Returns:
        int: The addition of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.

    Example:
        >>> add_integer(1, 2)
        3
        >>> add_integer(100, -2)
        98
        >>> add_integer(2)
        100
        >>> add_integer(100.3, -2)
        98
        >>> add_integer(4, "School")
        Traceback (most recent call last):
            ...
        TypeError: b must be an integer
        >>> add_integer(None)
        Traceback (most recent call last):
            ...
        TypeError: a must be an integer
    """

    if type(a) not in (int, float) or type(b) not in (int, float):
        if type(a) not in (int, float):
            raise TypeError("a must be an integer")
        if type(b) not in (int, float):
            raise TypeError("b must be an integer")

    return int(a) + int(b)
