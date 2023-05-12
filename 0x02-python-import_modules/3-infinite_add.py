#!/usr/bin/python3
import sys

if __name__ == "__main__":
    ac = len(sys.argv)
    word = sys.argv[1:]
    i = int(word)
    for i in word:
        if ac > 1:
            result = sum(i)
            print("{}".format(result))
        
    else:
        ac -= 1
        print("{}".format(ac))
