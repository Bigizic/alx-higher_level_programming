#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if my_list:
        for elements in range(len(my_list)):
            if my_list[elements] == 2:
                my_list[elements] = replace
        return my_list

