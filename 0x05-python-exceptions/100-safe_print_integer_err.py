#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        int_value = int(value)
        print("{:d}".format(int_value))
        return (True)
    except ValueError:
        print("Exception: Unknown format code 'd' for object of type 'str'", file=sys.stderr)
        return (False)
    except:
        print("Exception: Unknown format code 'd' for object of type 'str'", file=sys.stderr)
        return (False)
