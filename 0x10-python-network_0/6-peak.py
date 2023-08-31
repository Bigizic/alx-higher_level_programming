#!/usr/bin/python3
# a python module that finds the peak in a list of integers

def find_peak(list_of_integers):
    """Start
    """
    if len(list_of_integers) is 0:
        return None

    lis = list_of_integers
    peak = None

    if lis[0] >= lis[1] and lis[0] >= len(lis):
        return lis[0]

    for i in range(len(list_of_integers) - 1):
        if lis[i] >= lis[i - 1] and lis[i] >= lis[i + 1]:
            peak = lis[i]
    return peak
