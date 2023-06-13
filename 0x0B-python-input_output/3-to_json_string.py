#!/usr/bin/python3
import json

"""A function that returns the JSON representation of an object (string)

Parameters:
    my_obj (str)

Raises:
    Void

Return:
    JSON representation of an object
"""


def to_json_string(my_obj):
    result = json.dumps(my_obj, sort_keys=True)
    return result
