#!/usr/bin/python3
"""A function that returns the list of available attributes and methods
of an object

Parameters:
    obj (object) object containing attributes and methods

Return:
    A list object
"""


def lookup(obj):
    return dir(obj)
