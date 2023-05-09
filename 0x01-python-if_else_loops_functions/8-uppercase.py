#!/usr/bin/python3

def uppercase(str):
    return my_upp(str)

def my_upp(st):
    word = ""
    for i in st:
        if 97 <= ord(i) <= 122:
            word += chr(ord(i) - 32)
        else:
            word += i
            print("{}".format(word), end="")
            return word
