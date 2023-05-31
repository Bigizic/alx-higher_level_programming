#!/usr/bin/python3
"""Square class
a class Square that defines a square by: (based on 4-square.py)
plus Public instance method: def my_print(self): that prints in
stdout the square with the character #:
"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """Constructor"""
        self.size = size

    @property
    def size(self):
        """Getter"""
        return self.square_area

    @size.setter
    def size(self, value):
        """Setter"""
        if type(value) is int:
            if value >= 0:
                self.square_area = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.square_area == 0:
            print()
        for i in range(self.square_area):
            print("#" * self.square_area)

    def area(self):
        """Returns square area"""
        return self.square_area ** 2
