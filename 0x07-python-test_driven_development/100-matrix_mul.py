#!/usr/bin/ python3
"""Matrix Multiplication Module
a function that multiplies 2 matrices

Parameters:
    m_a (list) of integrs and float
    m_b (list) of integrs and float
"""


def matrix_mul(m_a, m_b):
    ma_list_error = "m_a must be a list of lists"
    mb_list_error = "m_b must be a list of lists"
    ma_empty_list = "m_a can't be empty"
    mb_empty_list = "m_b can't be empty"
    ma_wrong_type = "m_a should contain only integers or floats"
    mb_wrong_type = "m_b should contain only integers or floats"
    ma_rows_error = "each row of m_a must be of the same size"
    mb_rows_error = "each row of m_b must be of the same size"
    mul_error = "m_a and m_b can't be multiplied"

    """Get row and column of matrix a"""
    row_a = len(m_a[0])
    col_a = len(m_a)

    """Get row and column of matrix b"""
    row_b = len(m_b[0])
    col_b = len(m_b)

    if row_a != col_a:
        raise TypeError(ma_rows_error)
    if row_b != col_b:
        raise TypeError(mb_rows_error)

    if row_a != col_b:
        raise ValueError(mul_error)

    result = [[0 for i in range(row_b)] for i in range(col_a)]

    for items in range(col_a):
        for _item in range(row_b):
            for k in range(row_a):
                result[items][_item] += m_a[items][k] * m_b[k][_item]
    for row in result:
        return row
