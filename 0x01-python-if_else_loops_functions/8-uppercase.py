#!/usr/bin/python3

def uppercase(str):
    word = ""
    for x in str:
        if ord(x) > 96 and ord(x) < 123:
            word += chr(ord(x)-32)
        else:
            word += x
            print(word)
