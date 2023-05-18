#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for val in new_dict:
        new_dict[val] *= 2
    return new_dict
