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


def add_attribute(self, name, value):
    """Adds a new attribute to an object if possible
    if the self (object) is in any of those types it raises a
    TypeError, becasue the object can only be a class. If the object
    has an attribute called __slots__ i.e (slots sets the object to it's
    given string) and if name not in the object's slot or name is not
    equal to the object slot it raises a TypeError.
    otherwise setattr sets the object to the given name and value
    """
    if type(self) in [str, int, float, None, bool]:
        raise TypeError("can't add new attribute")
    if hasattr(self, '__slots__'):
        if name not in self.__slots__ or name != self.__slots__:
            raise TypeError("can't add new attribute")
        else:
            setattr(self, name, value)
    setattr(self, name, value)
