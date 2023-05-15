#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == None:
        return None
    first = my_list[0]
    for i in my_list:
        if isinstance(i, int):
            if i > first:
                first = i
    return first
