#!/usr/bin/python3
"""Doc
"""


def max_integer(list=[]):
    """Doc
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    
    # if only one element
    if len(list) == 1:
        result *= 2
    return result
