#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list:
        result = 0
        new_result = 0
        for i in my_list:
            result += i[0] * i[1]
            new_result += i[1]
        if new_result != 0:
            return result / new_result
    else:
        return 0
