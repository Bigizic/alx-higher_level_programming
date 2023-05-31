#!/usr/bin/python3
"""Square module that sets and gets
a class Square that defines a square by: (based on 3-square.py)
"""


class Square:
    """Square class"""

    def __init__(self, size=0):
        """Constructor
        Args:
            size int type
        Raises:
            TypeError: if size is not given as integer
            ValueError: if size is lesser than 0
        """

        self.size = size

    @property
    def size(self):
        """Getter
        retrieves square size by returning square size
        """

        return self.square_area

    @size.setter
    def size(self, value):
        """Setter
        sets square size to equal value
        """
        if type(value) is int:
            if value >= 0:
                self.square_area = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """A public insatnce method that returns the current square area"""

        return self.square_area ** 2
