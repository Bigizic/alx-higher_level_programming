#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    deleted_keys = []
    for i, x in a_dictionary.items():
        if x == value:
            deleted_keys.append(i)
    for i in deleted_keys:
        del (a_dictionary[i])
    return a_dictionary
