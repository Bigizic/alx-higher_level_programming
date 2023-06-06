#!/usr/bin/python3
"""A lazy Matrix Multiplication Module

Parameters:
    m_a (list) int or float types
    m_b (list) int or float types
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    result = np.matmul(m_a, m_b)
    return result
