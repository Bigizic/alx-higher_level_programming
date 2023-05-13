#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    l = len(my_list)
    l -= 1
    if idx < 0:
        return my_list
    if idx > l:
        return my_list
    my_list[idx] = element
    return my_list
