#!/usr/bin/python3
"""A function that appends a string at the end of a text file (UTF8)
and returns the number of characters added

Parameters:
    filename (txt) name of the file to write into
    text (str) text to be written

Raises:
    Void

Return:
    number of characters added
"""


def append_write(filename="", text=""):
    """Implementation
    """
    with open(filename, "a") as open_file:
        append_to_file = open_file.write(text)
        return len(text)
