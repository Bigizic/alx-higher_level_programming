#!/usr/bin/python3
"""A function that returns the JSON representation of an object (string)

Parameters:
    my_obj (str)

Raises:
    Void

Return:
    JSON representation of an object
"""
import json


def to_json_string(my_obj):
    """Implementation
    """
    result = json.dumps(my_obj)
    return result
