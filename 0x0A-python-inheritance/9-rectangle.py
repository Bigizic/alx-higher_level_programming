#!/usr/bin/python3
"""Class Module
A class Rectangle that inherits from BaseGeometry

Parameters:
    width (int) width of rectangle
    height (int) height of rectangle

Return:
    str() should return
    the following rectangle description:[Rectangle] <width>/<height>
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """SubClass of BaseGeometry
    """

    def __init__(self, width, height):
        """Constructor
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.my_width = width
        self.my_height = height

    def __str__(self):
        """Returns description
        """
        return ("[Rectangle] {}/{}" .format(self.my_width, self.my_height))

    def area(self):
        """returns area of rectangle
        """
        result = self.my_width * self.my_height
        return result
