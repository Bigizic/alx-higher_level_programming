#!/usr/bin/python3
"""Class Module
A class Rectangle that inherits from BaseGeometry

Parameters:
    width (int) width of rectangle
    height (int) height of rectangle

Return:
    Void
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """SubClass of BaseGeometry
    """
    def __init__(self, width, height):
        """constructor
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.my_width = width
        self.my_height = height
