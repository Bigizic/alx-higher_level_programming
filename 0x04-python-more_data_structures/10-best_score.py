#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        count = 0
        va_lues = list(a_dictionary.values())
        k_eys = list(a_dictionary.keys())
        first = va_lues[0]
        for i in va_lues:
            if i > first:
                first = i
        for x in va_lues:
            if first != x:
                count += 1
            else:
                break
        return k_eys[count]
    else:
        return None
