#!/usr/bin/python3
"""Class Module

Parameters:
    name (str) is always a string
    value (int)

Raises:
    Exception("area() is not implemented")
    TypeError("<name> must be an integer")
    ValueError("<name> must be greater than 0")

Return:
    Void
"""


class BaseGeometry:
    """class BaseGeometry
    """
    m = "must be an integer"
    n = "must be greater than 0"

    def area(self):
        """Raise exception message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Raises TypeError and ValueError"""
        if type(value) is not int:
            raise TypeError("{} {}" .format(name, self.m))

        if value <= 0:
            raise ValueError("{} {}" .format(name, self.n))
