#!/usr/bin/python3
def string_duplicate(string, n):
    result = string * n
    return result

def new_in_list(my_list, idx, element):
    word = string_duplicate(my_list, 1)
    list_length = len(my_list)
    list_length -= 1
    if idx < 0 or idx > list_length:
        return my_list
    word[idx] = element
    return word
