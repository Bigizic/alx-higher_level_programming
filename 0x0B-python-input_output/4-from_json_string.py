#!/usr/bin/python3
"""A function that returns an object (Python data structure)
represented by a JSON string

Parameters:
    my_str (JSON string)

Raises:
    void

Return:
    an object(Python data structure)
"""
import json


def from_json_string(my_str):
    """Implementation
    """
    return(json.loads(my_str))
