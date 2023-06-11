#!/usr/bin/python3
"""A function that returns True if the object is an instance of, or if
the object is an instance of a class that inherited from, the specified
class, otherwise False

Parameters:
    obj (object) to be compared
    a_class (class) specified class

Return:
    (True) if the object is an instance of class inherited from
    (False) otherwise
"""


def is_kind_of_class(obj, a_class):
    """is_kind_of_class implementation"""
    if type(obj) is a_class or isinstance(obj, a_class):
        return True
    else:
        return False
