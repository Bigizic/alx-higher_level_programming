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
    def width(self):
        """Width Getter, Also retrives the width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """Width Setter, Sets the Width to a value
        """
        if type(value) is int:
            if value > 0:
                self.__width = value
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """Height Getter, Also retrives the height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """Height setter, Sets the height to a value
        """
        if type(value) is int:
            if value > 0:
                self.__height = value
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        """X Getter, Also retrives element x
        """
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
    def y(self):
        """Y Getter, Also retrives element y
        """
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

    def display(self):
        """Prints in stdout the Rectangle instance with the character #
        """
        x = self.__width
        y = self.__height

        for i in range(y):
            print("#" * x)
