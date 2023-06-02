#!/usr/bin/python3
"""Addition Module
A function that adds two integers, a and b must be integers or float,
otherwise raise a TypeError, a and b must be casted to integers if they
are float
"""


def add_integer(a, b=98):
    """
    Parameters:
        a (int or float) type
        b (int or float) type
    """

    if type(a) in [int, float]:
        try:
            a = int(a)
        except Exception:
            raise TypeError("a must be an integer")
    else:
        raise TypeError("a must be an integer")

    if type(b) in [int, float]:
        try:
            b = int(b)
        except Exception:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("b must be an integer")

    return a + b
