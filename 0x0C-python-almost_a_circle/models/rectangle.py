#!/usr/bin/python3
"""Class Module
A class Rectangle that inherits from Base

Parameters:
    width (int) width of rectangle
    height (int) height of rectangle
    x (int)
    y (int)
    id (int)

Raises:
    Void

Return:
    Void
"""

from models.base import Base


class Rectangle(Base):
    """Subclass Rectangle

    Private instance attribute, each with its own public getter and setter
    __width -> width
    __height -> height
    __x -> x
    __y -> y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    """Width Getter, Also retrives the width
    """
    def width(self):
        return (self.__width)

    @width.setter
    """Width Setter, Sets the Width to a value
    """
    def width(self, value):
        if type(value) is int:
            if value > 0:
                self.__width = value
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

    @property
    """Height Getter, Also retrives the height
    """
    def height(self):
        return (self.__height)

    @height.setter
    """Height setter, Sets the height to a value
    """
    def height(self, value):
        if type(value) is int:
            if value > 0:
                self.__height = value
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")

    @property
    """X Getter, Also retrives element x
    """
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, value):
        """X Setter, Sets the x element to a value
        """
        if type(value) is int:
            if value >= 0:
                self.__x = value
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")

    @property
    """Y Getter, Also retrives element y
    """
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, value):
        """Y Setter, Sets the y element to a value
        """
        if type(value) is int:
            if value >= 0:
                self.__y = value
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")

    def area(self):
        """Returns the area of the rectangle
        """
        return self.__width * self.__height
