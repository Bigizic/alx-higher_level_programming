#!/usr/bin/python3
"""Print Square Module

Parameters:
    size (int) is the size length of the square
"""


def print_square(size):
    """
    A function that prints a square with the character # multiplied by size
    Raises:
        TypeError
        ValueError
    Return:
        void
    """
    if type(size) is float and size < 0:
        try:
            raise TypeError("size must be an integer")
        except Exception:
            raise TypeError("size must be an integer")
    else:
        size = size

    if type(size) is not int:
        try:
            raise TypeError("size must be an integer")
        except Exception:
            raise TypeError("size must be an integer")
    else:
        size = size

    if size < 0:
        try:
            raise ValueError("size must be >= 0")
        except Exception:
            raise ValueError("size must be >= 0")
    else:
        size = size

    for items in range(size):
        print("#" * size)
