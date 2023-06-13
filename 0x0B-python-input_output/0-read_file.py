#!/usr/bin/python3
"""A function that reads a text file(UTF8) and prints it to stdout

Parameters:
    filename (txt) file name to read

Raises:
    Void

Return:
    Void
"""


def read_file(filename=""):
    """Implementation
    """
    with open(filename, "r") as open_file:  # Open file
        read_file = open_file.read()  # put opened file in read mode
        print(read_file, end="")  # print opened file to stdout
