#!/usr/bin/python3
"""A function that inserts a line of text to a file, after each line
containing a specific string

Parameters:
    filename (txt) file to open
    search_string (str) string to search in file
    new_string (str) updates searched string to it's self

Raises:
    Void

Return:
    same file with search_string that was found updated to new_string
"""


def append_after(filename="", search_string="", new_string=""):
    """Opens file for reading, read each lines of opened file
        open same file for writing, iterate through each characters
        of file already read, write each characters to the write
        operation, search for string in line if found, write the new
        string to the write operation
    """
    with open(filename, "r") as open_file:
        read_file = open_file.readlines()

    with open(filename, "w") as open_files:
        for line in read_file:
            open_files.write(line)
            if search_string in line:
                open_files.write(new_string)
