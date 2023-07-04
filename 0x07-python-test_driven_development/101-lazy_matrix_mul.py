#!/usr/bin/python3
# 101-lazy_matrix_mul.py
"""multiplies 2 matrices by using the module NumPy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """the multiplication of the two matrices are returned.

    Args:
        m_a (list of lists of ints/floats): is the first matrix.
        m_b (list of lists of ints/floats): is the second matrix.
    """

    return (np.matmul(m_a, m_b))
