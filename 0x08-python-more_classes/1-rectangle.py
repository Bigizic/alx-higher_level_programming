#!/usr/bin/python3
"""Class Module
A class Rectangle that defines a rectangle : (based on 0-rectangle.py)

Parameters:
    width (int) width of rectangle
    height (int) height of rectangle
"""


class Rectangle:
    """Rectangle Class"""

    def __init__(self, width=0, height=0):
        """Constructor"""
        self.height = height
        self.width = width

    @property
    def height(self):
        """Height Getter"""
        return self._Rectangle__height

    @height.setter
    def height(self, value):
        """Height Setter"""
        if type(value) is int:
            if value >= 0:
                self._Rectangle__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def width(self):
        """Width Getter"""
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        """Width Setter"""
        if type(value) is int:
            if value >= 0:
                self._Rectangle__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")
