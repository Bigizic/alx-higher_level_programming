#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        count = 0
        v = list(a_dictionary.values())
        k = list(a_dictionary.keys())
        first = v[0]
        for i in v:
            if i > first:
                first = i
        for x in v:
            if first != x:
                count += 1
            else:
                break
            
        return k[count]
    else:
        return None
