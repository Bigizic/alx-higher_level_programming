#!/usr/bin/python3
"""A function that writes a string to a text file (UTF8)
and returns the number of characters written

Parameters:
    filename (txt) name of the file to write into
    text (str) text to be written

Raises:
    void

Return:
    number of characters written
"""


def write_file(filename="", text=""):
    """Implementation
    """
    with open(filename, "w") as open_file:
        write_to_file = open_file.write(text)
        return len(text)
