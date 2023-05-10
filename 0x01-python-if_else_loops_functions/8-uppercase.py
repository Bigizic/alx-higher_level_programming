#!/usr/bin/python3
def my_upper(string):
    res = ""
    for char in string:
        if 'a' <= char <= 'z':
            res += chr(ord(char) - 32)
        else:
            res += char
    return res


def uppercase(str):
    word = str.lower()
    new_word = my_upper(word)
    print("{}".format(new_word))
