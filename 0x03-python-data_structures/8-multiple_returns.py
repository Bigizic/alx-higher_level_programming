#!/usr/bin/python3
def multiple_returns(sentence):
    l = len(sentence)
    f = sentence[0]
    if sentence is None:
        f = None
    return l, f
