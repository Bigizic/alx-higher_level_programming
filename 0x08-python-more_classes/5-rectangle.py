#!/usr/bin/python3
"""Class Module

Parameters:
    width (int) width of rectangle
    height (int) height of rectangle
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
        """Returns the rectangle perimeter"""
        if self.rectangle_height is 0 or self.rectangle_width is 0:
            return 0
        return 2 * (self.rectangle_height + self.rectangle_width)

    def __str__(self):
        if self.rectangle_height is 0 or self.rectangle_width is 0:
            return ""
        else:
            rec_str = ""
            for i in range(self.rectangle_height):
                rec_str += "#" * self.rectangle_width + "\n"
        return rec_str[:-1]

    def __repr__(self):
        return f"Rectangle({self.rectangle_width}, {self.rectangle_height})"

    def __del__(self):
        print("Bye rectangle...")
