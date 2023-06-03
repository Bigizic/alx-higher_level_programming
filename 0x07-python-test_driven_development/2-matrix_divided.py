#!/usr/bin/python3
"""Matrix Division Module
a function that divides all elements of a matrix

Parameters:
    matrix(list of intgers or float)
    div(integer or float)
"""


def matrix_divided(matrix, div):
    matrix_error = "matrix must be a matrix (list of lists) of integers/floats"
    row_error = "Each row of the matrix must have the same size"
    div_number_error = "div must be a number"
    div_zero_error = "division by zero"

    if type(matrix) is list:
        try:
            row_length = len(matrix[0])
            new_matrix = []
            for rows in matrix:
                if len(rows) == row_length:
                    try:
                        new_row = []
                        for elements in rows:
                            if type(elements) in [int, float]:
                                try:
                                    if type(div) in [int, float]:
                                        try:
                                            if div != 0:
                                                try:
                                                    new_element = round(elements / div, 2)
                                                    new_row.append(new_element)
                                                except Exception:
                                                    raise ZeroDivisionError(div_zero_error)
                                            else:
                                                raise ZeroDivisionError(div_zero_error)
                                        except Exception:
                                            raise TypeError(div_number_error)
                                    else:
                                        raise TypeError(div_number_error)
                                except Exception:
                                    raise TypeError(matrix_error)
                            else:
                                raise TypeError(matrix_error)
                        new_matrix.append(new_row)
                    except Exception:
                        raise TypeError(row_error)
                else:
                    raise TypeError(row_error)
        except Exception:
            raise TypeError(matrix_error)
    else:
        raise TypeError(matrix_error)

    return new_matrix
