#!/usr/bin/python3
"""Square module
Class square that defines a square by: (based on 1-square.py)
"""


class Square:
    """Class square"""

    def __init__(self, size=0):
        """Sets the attributes for square object
        Args:
            Size (int) type
        Raises:
            TypeError: if size is not given as integer
            ValueError: if size is less than 0
        """
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
