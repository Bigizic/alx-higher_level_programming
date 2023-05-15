#!/usr/bin/python3
def element_at(my_list, idx):
    l = len(my_list)
    if idx < 0:
        return None
    if idx >= l:
        return None
    return my_list[idx]
