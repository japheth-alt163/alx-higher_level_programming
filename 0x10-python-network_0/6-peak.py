#!/usr/bin/python3
"""
Finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(list): List of integers to find peak of
    Returns:
        int: Peak of list_of_integers or None
    """
    size = len(list_of_integers)
    mid = size // 2
    mid_e = mid // 2

    if size == 0:
        return None

    while mid_e > 0:
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            mid = mid + mid_e
        elif list_of_integers[mid] < list_of_integers[mid - 1]:
            mid = mid - mid_e
        else:
            return list_of_integers[mid]
        mid_e = max(mid_e // 2, 1)

    return list_of_integers[mid]
