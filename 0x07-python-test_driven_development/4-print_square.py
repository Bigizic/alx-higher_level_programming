#!/usr/bin/python3
"""Print Square Module
a function that prints a square with the character #
(size) is the size length of the square
size must be an integer, otherwise raise a TypeError
if size is less than 0, raise a ValueError
if size is a float and is less than 0, raise a TypeError
"""


def print_square(size):
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
