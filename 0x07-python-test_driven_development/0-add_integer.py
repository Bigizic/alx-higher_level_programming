#!/usr/bin/python3
"""Addition Module
a function that adds 2 integers, a and b must be integers or floats,
otherwise it raise a TypeError, a and b must be first casted to
integers if they are float, Returns an integer: the addition of a and b


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
