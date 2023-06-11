#!/usr/bin/python3
"""A function that returns True if the object is excatly an instance of
the specified class otherwise False

Parameters:
    obj (object) object to be compared
    a_class (class) specified class

Return:
    (True) if the object is exactly an instance of the specified class
    (False) otherwise
"""


def is_same_class(obj, a_class):
    """is_same_class implementation"""
    if type(obj) is not a_class:
        return False
    else:
        return True
