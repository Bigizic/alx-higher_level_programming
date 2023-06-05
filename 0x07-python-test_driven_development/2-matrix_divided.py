#!/usr/bin/python3
"""Matrix Division Module
parameters:
    matrix(list of intgers or float)
    div(integer or float)
"""


def matrix_divided(matrix, div):
    """
    a function that divides all elements of a matrix by a float or int
    Raises:
        TypeError
        ZeroDivisionError
    Return:
        new matrix
    """

    matrix_error = "matrix must be a matrix (list of lists) of integers/floats"
    row_error = "Each row of the matrix must have the same size"
    div_number_error = "div must be a number"
    div_zero_error = "division by zero"

    if type(matrix) is not list:
        try:
            raise TypeError(matrix_error)
        except Exception:
            raise TypeError(matrix_error)
    else:
        matrix = matrix

    if type(matrix[0]) is not list and len(matrix) > 0:
        try:
            raise TypeError(matrix_error)
        except Exception:
            raise TypeError(matrix_error)
    else:
        matrix = matrix

    if type(div) not in [int, float]:
        try:
            raise TypeError(div_number_error)
        except Exception:
            raise TypeError(div_number_error)
    else:
        div = div

    if div == 0:
        try:
            raise ZeroDivisionError(div_zero_error)
        except Exception:
            raise ZeroDivisionError(div_zero_error)
    else:
        div = div

    row_length = len(matrix[0])
    new_matrix = []

    for rows in matrix:
        if len(rows) != row_length:
            try:
                raise TypeError(row_error)
            except Exception:
                raise TypeError(row_error)
        else:
            new_row = []

        for elements in rows:
            if type(elements) not in [int, float]:
                try:
                    raise TypeError(matrix_error)
                except Exception:
                    raise TypeError(matrix_error)
            else:
                new_element = round(elements / div, 2)
                new_row.append(new_element)
        new_matrix.append(new_row)
    return new_matrix
