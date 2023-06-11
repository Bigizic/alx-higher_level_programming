#!/usr/bin/python3
"""A function that returns True if the object is an instance of a class
that inherited (directly or indirectly) from the specified class,
otherwise False

Parameters:
    obj (object) to be compared
    a_class (class) specified class

Return:
    (True) if the object is an instance of a class that inherited
    (False) otherwise
"""


def inherits_from(obj, a_class):
    """inherits_from implementation"""
    if type(obj) is not a_class or not isinstance(obj, a_class):
        return True
    else:
        return False