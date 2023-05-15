#!/usr/bin/python3

def element_at(my_list, idx):
    l = len(my_list)
    if idx < 0 or idx >= l:
        return None
    else:
        return my_list[idx]
