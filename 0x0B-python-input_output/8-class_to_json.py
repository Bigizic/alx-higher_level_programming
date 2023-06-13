#!/usr/bin/python3
"""A function that returns the dictionary description with simple data
structure (list, dictionary, string, integer and boolean) for JSON
serialization of an object

Parameters:
    obj (class) instance of a class

Raises:
    Void

Return:
     the dictionary description with simple data structure
"""


def class_to_json(obj):
    """Implementation
    """
    a = vars(obj)
    return a
