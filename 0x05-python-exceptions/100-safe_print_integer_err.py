#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return (True)
        else:
            error_msg = "Exception: Unknown format code 'd' for object of type 'str'"
            print(error_msg, file=sys.stderr)
            raise TypeError(error_msg)
            return (False)
    except TypeError:
        pass
