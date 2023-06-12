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
        self.my_size = size

    def __str__(self):
        """Return description
        """
        return ("[Square] {:d}/{:d}".format(self.my_size, self.my_size))
