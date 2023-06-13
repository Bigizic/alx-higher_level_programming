#!/usr/bin/python3
"""A function that writes an Object to a text file, using a JSON
representation

Parameters:
    my_obj (str) object to write
    filename (json) file to write into

Rasises:
    Void

Return:
    Void
"""
import json


def save_to_json_file(my_obj, filename):
    """Implementation
    """
    with open(filename, "w") as open_file:
        obj = json.dumps(my_obj)
        write_to_file = open_file.write(obj)
