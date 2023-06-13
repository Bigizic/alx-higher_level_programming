#!/usr/bin/python3
"""A function that adds a new attribute to an object if it’s possible

Parameters:
    Void

Raises:
    TypeError("can't add new attribute")  if the object can’t
    have new attribute

Return:
    Void
"""


def add_attribute(obj, name, value):
    """Adds a new attribute to an object if possible
    if the object is a string or in any of those types it raises a
    TypeError or if the object has the class attribute
    otherwise setattr sets the object to the given name and value
    """
    if (type(obj) in [str, int, float, None, bool] or
            hasattr(obj, '__class__')):
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
