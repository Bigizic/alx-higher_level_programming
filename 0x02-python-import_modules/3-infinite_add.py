#!/usr/bin/python3
import sys

def my_function():
    ac = len(sys.argv)
    word = sys.argv[1:]

    if (ac > 1):
        result = sum(int(i) for i in word)
        print("{}" .format(result))
        
    else:
        ac -= 1
        print("{}" .format(ac))

if __name__ == "__main__":
    my_function()
