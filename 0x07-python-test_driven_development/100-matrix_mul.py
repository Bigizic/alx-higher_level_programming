#!/usr/bin/python3
"""Matrix Multiplication Module
a function that multiplies 2 matrices

Parameters:
    m_a (list) of integrs and float
    m_b (list) of integrs and float
"""


def matrix_mul(m_a, m_b):
    """Errors to display"""
    ma_error_1 = "m_a must be a list"
    mb_error_1 = "m_b must be a list"
    ma_list_error = "m_a must be a list of lists"
    mb_list_error = "m_b must be a list of lists"
    ma_empty_list = "m_a can't be empty"
    mb_empty_list = "m_b can't be empty"
    ma_wrong_type = "m_a should contain only integers or floats"
    mb_wrong_type = "m_b should contain only integers or floats"
    ma_rows_error = "each row of m_a must be of the same size"
    mb_rows_error = "each row of m_b must be of the same size"
    mul_error = "m_a and m_b can't be multiplied"

    # a check if m_a and m_b are either strings
    if type(m_a) is str:
        raise TypeError(ma_error_1)

    if type(m_b) is str:
        raise TypeError(mb_error_1)

    # a check if either matrix are not a list or list of list
    if type(m_a) is not list or not all(isinstance(row, list) for row in m_a):
        raise TypeError(ma_list_error)

    if type(m_b) is not list or not all(isinstance(row, list) for row in m_b):
        raise TypeError(mb_list_error)

    # a check if either matrix are a nested list i.e [[]]
    if len(m_a) == 1 and len(m_a[0]) == 0:
        raise ValueError(ma_empty_list)

    if len(m_b) == 1 and len(m_b[0]) == 0:
        raise ValueError(mb_empty_list)

    # a check if either list is empty
    if len(m_a) == 0:
        raise ValueError(ma_empty_list)

    if len(m_b) == 0:
        raise ValueError(mb_empty_list)

    # a check if all elements in either matrics are float or int types
    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError(ma_wrong_type)

    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError(mb_wrong_type)

    # a check if either matrics have the same length of row
    if len(set(len(row) for row in m_a)) != 1:
        raise TypeError(ma_rows_error)

    if len(set(len(row) for row in m_b)) != 1:
        raise TypeError(mb_rows_error)

    # Get row and column of matrix a
    row_a = len(m_a)
    col_a = len(m_a[0])

    # Get row and column of matrix b
    row_b = len(m_b)
    col_b = len(m_b[0])

    if col_a != row_b:
        raise ValueError(mul_error)

    result = [[0 for i in range(col_b)] for i in range(row_a)]

    for i in range(row_a):
        for j in range(col_b):
            for k in range(col_a):
                # Final Result
                result[i][j] += m_a[i][k] * m_b[k][j]

    """A check if the result contain float types that is/are not
    2 decimal places after the multiplication
    """
    for i in range(len(result)):
        for j in range(len(result[0])):
            if isinstance(result[i][j], float):
                result[i][j] = round(result[i][j], 2)
    return result
