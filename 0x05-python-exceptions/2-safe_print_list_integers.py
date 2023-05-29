#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in my_list:
            if not isinstance(i, int):
                continue
            if count < x:
                print("{:d}".format(i), end="")
                count += 1
            else:
                break
        print()
    except nothing:
        pass
    return (count)
