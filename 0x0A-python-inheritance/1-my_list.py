#!/usr/bin/python3
"""A Class Module

A class MyList that inherits frm list

Parameters:
    None

Return:
    Void
"""


class MyList(list):
    """Subclass of list"""
    def __init__(self):
        """Constructor"""
        super().__init__()

    def print_sorted(self):
        """Print the sorted list"""
        print(sorted(self))
