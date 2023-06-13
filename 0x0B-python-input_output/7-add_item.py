#!/usr/bin/python3
"""A script that adds all arguments to a Python list, and then save them
to a file

Parameters:
    args

Raises:
    void

Description:
    The script attempts to open a file if the file is not found it sets
the argument to an empty list, it proceed to append the arguments in
stdin to the argument variable then proceed to add the argument to the
save_to_jason function, btw this save_to_jason function sets the filename
to write mode, so if the file doesn't exit it creates it, so while the
file couldn't be read by the load_from_jason function the save_to_jason
creates the file then the load_from_jason returns the content in the file
since it has been created.

Return:
    void
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

stdin_arg = sys.argv[1:]
filename = "add_item.json"
argument = []

try:
    argument = load_from_json_file(filename)
except Exception:
    argument = []

for items in stdin_arg:
    argument.append(items)
save_to_json_file(argument, filename)
