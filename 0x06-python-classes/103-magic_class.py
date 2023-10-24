#!/usr/bin/python3
"""Magic class from given ByteCode."""
import math


class MagicClass:
    """Initialization of MagicClass."""
    def __init__(self, radius=0):
        """Initialization of data."""
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """Calculation of area."""
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """Calculation of the circumference."""
        return 2 * math.pi * self._MagicClass__radius
