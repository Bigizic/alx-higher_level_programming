#!/usr/bin/python3
"""Class Module
A class that returns the area of a rectangle and the perimeter
Parameters:
    width (int) width of a rectanle
    height (int) height of a rectangle
"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """Constructor"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Width Getter"""
        return self.rectangle_width

    @width.setter
    def width(self, value):
        """Width Setter"""
        if type(value) is int:
            if value >= 0:
                self.rectangle_width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """Height Getter"""
        return self.rectangle_height

    @height.setter
    def height(self, value):
        if type(value) is int:
            if value >= 0:
                self.rectangle_height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """Returns the rectangle area"""
        return self.rectangle_height * self.rectangle_width

    def perimeter(self):
        """Reutrns the rectangle perimeter"""
        if self.rectangle_height is 0 or self.rectangle_width is 0:
            return 0
        return 2 * (self.rectangle_height + self.rectangle_width)
