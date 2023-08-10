#!/usr/bin/python3
""" A Technical interview preparation
        Pascal Triangle
"""


def pascal_triangle(n):
    """Implementation
    """
    res = []

    for i in range(n):
        tmp = []
        for x in range(i + 1):
            if x == 0 or x == i:
                tmp.append(1)
            else:
                tmp.append(res[i - 1][x - 1] + res[i - 1][x])
        res.append(tmp)
    return res
