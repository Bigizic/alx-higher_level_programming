#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        count = 0
        valu = list(a_dictionary.values())
        key = list(a_dictionary.keys())
        first = valu[0]
        for i in valu:
            if i > first:
                first = i
        for x in valu:
            if first != x:
                count += 1
            else:
                break
            
        return key[count]
    else:
        return None
