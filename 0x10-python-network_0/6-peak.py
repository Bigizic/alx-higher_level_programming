#!/usr/bin/python3
"""a python module that finds the peak in a list of integers
"""


def find_peak(list_of_integers):
    """Start
    """
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) <= 2:
        return max(list_of_integers)

    lis = list_of_integers
    left = 0
    right = len(lis) - 1
    while left < right:
        mid = left + (right - left) // 2
        if lis[mid] < lis[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return lis[left]
