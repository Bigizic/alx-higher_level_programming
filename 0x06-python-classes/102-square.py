#!/usr/bin/python3
"""Square module.
 a class Square that defines a square by: (based on 4-square.py)
"""


class Square():
    """Square class"""

    def __init__(self, size=0):
        """Constructor
        Args:
            size int type
        """
        self.size = size

    def __eq__(self, other):
        """Set the Compare equality behavior of square object
        """
        if type(other) is Square:
            return self.area() == other.area()

    def __lt__(self, other):
        """Set the compare less than behavior of the Square object
        """
        if type(other) is Square:
            return self.area() < other.area()

    def __le__(self, other):
        """Sets the compare less equal than behavior of the Square object
        """
        if type(other) is Square:
            return self.area() <= other.area()

    @property
    def size(self):
        """Get or set the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Returns the current square area"""

        return self.__size ** 2
