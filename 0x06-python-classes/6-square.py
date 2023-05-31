#!/usr/bin/python3
"""Square module
 a class Square that defines a square by: (based on 5-square.py)
 Public instance method: def my_print(self): that prints in stdout
 the square with the character #:
 if size is equal to 0, print an empty line
 position should be use by using space - Don’t fill lines by spaces when
 position[1] > 0
 """


class Square:
    """Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Position getter"""
        return self.square_position

    @position.setter
    def position(self, value):
        """Position setter"""
        if (type(value) is tuple and len(value) is 2 and
                type(value[0]) is int and type(value[1]) is int and
                value[0] >= 0 and value[1] >= 0):
            self.square_position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """Prints in stdout the square with the character #"""
        x = self.square_position[0]
        y = self.square_position[1]

        if self.square_area > 0:
            for elements in range(y):
                print()
            for elements in range(self.square_area):
                print(" " * x, end="")
                print("#" * self.square_area)

        else:
            print()

    def area(self):
        """Returns square area"""
        return self.square_area ** 2
