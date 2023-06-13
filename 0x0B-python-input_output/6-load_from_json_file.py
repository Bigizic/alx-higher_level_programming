#!/usr/bin/python3
"""A function that creates an Object from a “JSON file”

Parameters:
    filename (json) file to open for reading

Raises:
    void

Return:
    Void
"""
import json


def load_from_json_file(filename):
    """Implementation
    """
    with open(filename, "r") as open_file:
        cp_read = open_file.read()
        return json.loads(cp_read)
