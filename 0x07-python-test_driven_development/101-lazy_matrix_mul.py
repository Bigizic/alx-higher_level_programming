#!/usr/bin/python3
"""Numpy list multiplication module

Parameters:
    m_a (list of list of int/floats) first matrix
    m_b (list of list of int/floats) second matrix

Raises:
    Void
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Returns the multiplication of two matrices
    """
    result = np.matmul(m_a, m_b)
    return result
