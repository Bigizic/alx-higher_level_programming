#!/usr/bin/python3
def multiple_returns(sentence):
    list_len = len(sentence)
    first = sentence[0]
    if list_len == 0:
        first = None
    x = (list_len, first)
    return x
