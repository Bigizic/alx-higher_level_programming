#!/usr/bin/python3
"""A Class Module

A class MyList that inherits frm list

Parameters:
    None

Return:
    Void
"""


class MyList(list):
    """MyList Class"""

    def print_sorted(self):
        print(sorted(self))
