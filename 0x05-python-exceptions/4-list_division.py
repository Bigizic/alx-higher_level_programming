#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    div = False
    max_range = False
    w_type = False
    try:
        for index, element in enumerate(my_list_1):
            if not isinstance(element, (int, float)):
                my_list_1[index] = 0
                w_type = True
        for i, e in enumerate(my_list_2):
            if not isinstance(e, (int, float)):
                my_list_2[i] = 0
                w_type = True
        for x in range(list_length):
            if x >= len(my_list_1) or x >= len(my_list_2):
                result = 0
                max_range = True
            elif my_list_2[x] == 0:
                result = 0
                div = True
            else:
                result = my_list_1[x] / my_list_2[x]

            new_list.append(result)
    except nothing:
        pass
    finally:
        if div:
            print("division by 0")
        if w_type:
            print("wrong type")
        if max_range:
            print("out of range")
        return new_list
