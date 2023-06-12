#!/usr/bin/python3
"""Class Module
A class MyInt that inherits frm int
MyInt is a rebel. MyInt has == and != operators inverted

Parameters:
    value (int) value to compare
    other (int) value to compare

Return:
    (False) if int value is != other
    (True) otherwise
"""


class MyInt(int):
    """Subclass of int
    """
    def __init__(self, value):
        """Constructor
        """
        self.value = value

    def __eq__(self, other):
        """Returns False
        """
        return self.value != other

    def __ne__(self, other):
        """Returns True
        """
        return self.value == other
