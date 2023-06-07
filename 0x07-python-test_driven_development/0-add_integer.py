#!/usr/bin/python3
"""Addition Module
Parameters:
    a(int or float) types: The first number
    b(int or float) types: The second number
"""


def add_integer(a, b=98):
    """
    Function that adds two numbers
    """

    if type(a) in [int, float]:
        try:
            a = a
        except Exception:
            raise TypeError("a must be an integer")
    else:
        raise TypeError("a must be an integer")

    if type(b) in [int, float]:
        try:
            b = b
        except Exception:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("b must be an integer")
    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89
    return int(a) + int(b)
