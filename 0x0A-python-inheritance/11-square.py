#!/usr/bin/python3
"""Class Module
A class Square that inherits from Rectangle (9-rectangle.py)
(task based on 10-square.py)

Parameters:
    size (int) size of square

Return:
    void
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Subclass of Rectangle
    """

    def __init__(self, size):
        """Constructor
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
