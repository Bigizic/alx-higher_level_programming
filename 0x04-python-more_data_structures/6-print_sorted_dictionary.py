#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary.keys())
    for i in sorted_keys:
        values = a_dictionary[i]
        print(f"{i}: {values}")
