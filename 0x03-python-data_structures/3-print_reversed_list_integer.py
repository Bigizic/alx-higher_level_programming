#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        word = my_list[::-1]
        for i in word:
            print("{:d}".format(i))
