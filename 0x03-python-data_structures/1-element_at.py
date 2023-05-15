#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    l = len(my_list)
    if idx >= l:
        return None
    return my_list[idx]
