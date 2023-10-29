#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.

    Args:
    matrix (list of lists): The matrix containing integers or floats.
    div (int or float): The divisor.

    Returns:
    list of lists: A new matrix with elements rounded to 2 decimal places.

    Raises:
    TypeError:
        - If the matrix is not a list of lists of integers or floats, with the message
          "matrix must be a matrix (list of lists) of integers/floats".
        - If each row of the matrix does not have the same size, with the message
          "Each row of the matrix must have the same size".
        - If div is not a number (integer or float), with the message "div must be a number".
    ZeroDivisionError:
        - If div is equal to 0, with the message "division by zero".

    Example:
    >>> matrix = [[1, 2, 3], [4, 5, 6]]
    >>> matrix_divided(matrix, 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    """

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [
        [round(element / div, 2) for element in row]
        for row in matrix
    ]
    return new_matrix
