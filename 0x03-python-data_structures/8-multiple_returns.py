#!/usr/bin/python3
def multiple_returns(sentence):
    list_len = len(sentence)
    for i in sentence:
        first = sentence[0]
    if sentence is None:
        first = None
        list_len = None
    x = (list_len, first)
    return x
