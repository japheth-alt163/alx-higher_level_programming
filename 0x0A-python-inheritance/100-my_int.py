#!/usr/bin/python3
"""Defines the MyInt class, a rebel integer."""


class MyInt(int):
    """Represents a rebel integer with inverted == and != operators."""

    def __eq__(self, other):
        """
        Override the equality (==) operator.

        Args:
        other: The other integer to compare.

        Returns:
        True if the values are not equal; otherwise, False.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the inequality (!=) operator.

        Args:
        other: The other integer to compare.

        Returns:
        True if the values are equal; otherwise, False.
        """
        return super().__eq__(other)
