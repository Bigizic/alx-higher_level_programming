#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    word = my_list * 1
    list_length = len(my_list)
    if idx < 0 or idx >= list_length:
        return my_list
    word[idx] = element
    return word
