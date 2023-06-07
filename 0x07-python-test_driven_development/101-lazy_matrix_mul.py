#!/usr/bin/python3
"""Numpy list multiplication module"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    result = np.matmul(m_a, m_b)
    return result
