#!/usr/bin/python3
"""Print name Module
 a function that prints My name is <first name> <last name>
 first_name and last_name must be strings otherwise, raise a TypeError
"""


def say_my_name(first_name, last_name=""):
    if type(first_name) is not str:
        try:
            raise TypeError("first_name must be a string")
        except Exception:
            raise TypeError("first_name must be a string")
    else:
        first_name = first_name

    if type(last_name) is not str:
        try:
            raise TypeError("last_name must be a string")
        except Exception:
            raise TypeError("last_name must be a string")
    else:
        last_name = last_name
    print("My name is {} {}" .format(first_name, last_name))
