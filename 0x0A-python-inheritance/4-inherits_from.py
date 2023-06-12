#!/usr/bin/python3
"""A function that returns True if the object is an instance of a class
that inherited (directly or indirectly) frm the specified class,
otherwise False

Parameters:
    obj (object) to be compared
    a_class (class) specified class

Return:
    (True) if the object is an instance of a class that inherited
    (False) otherwise
"""


def inherits_from(obj, a_class):
    """implementation"""
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
