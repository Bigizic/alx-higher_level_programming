#!/usr/bin/python3
"""Class Module
A class MyInt that inherits frm int

Parameters:
    Void

Return:
    Void
"""


class MyInt(int):
    """Subclass of int
    """
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value != other

    def __ne__(self, other):
        return self.value == other

