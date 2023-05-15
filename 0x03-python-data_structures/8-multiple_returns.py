#!/usr/bin/python3
def multiple_returns(sentence):
    list_len = len(sentence)
    for i in sentence:
        f = sentence[0]
    if sentence is None:
        f = None
        list_len = None
    return list_len, f
