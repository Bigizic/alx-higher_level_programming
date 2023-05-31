#!/usr/bin/python3
"""Square module
a class Square that defines a square by: (based on 2-square.py)
"""


class Square:
    """Square class"""

    def __init__(self, size=0):
        """Sets the attributes for square object
        Args:
            Size (int) type
        Raises:
            TypeError: if size is not given as integer
            ValueError: is size is less than 0
        """

        if type(size) is int:
            if size >= 0:
                self.new_size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """A public insatnce method that returns the current square area"""

        return self.new_size ** 2
