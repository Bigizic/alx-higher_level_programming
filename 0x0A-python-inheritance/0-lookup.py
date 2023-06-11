#!/usr/bin/python3
"""A function that returns the list of available attributes and methods
of an object

Parameters:
    obj (object) object containing attributes and methods

Return:
    A list object
"""


def lookup(obj):
    """dir() function is used to retrive a list of names in the object's
    current namespace, It returns a sorted list of strings that includes
    the names of attributws, methods and other objects that are defined
    for the object
    """
    return dir(obj)
