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
    Used hasattr to check if the object has an attribute with the name,
    if yes it raises a typeerror
    otherwise setattr sets the object to the given name and value
    """
    if type(obj) in [str, int, float, None, bool]:
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
