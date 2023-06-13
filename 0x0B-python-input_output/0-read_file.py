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
    open_file = open(filename)  # Open file
    read_file = open_file.read()  # put opened file in read mode
    print(read_file)  # print opened file to stdout
    open_file.close()  # close file after open operation
