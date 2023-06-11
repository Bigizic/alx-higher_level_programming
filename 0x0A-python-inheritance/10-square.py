#!/usr/bin/python3
"""Class Module
A class Square that inherits from Rectangle (9-rectangle.py)

Parameters:
    size (int) size of square

Return:
    Void
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square
    """

    def __init__(self, size):
        """Constructor
        """
        self.integer_validator("size", size)
        self.my_size = size
        super().__init__(size, size)
