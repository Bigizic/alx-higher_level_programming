#!/usr/bin/python3
import sys

if __name__ == "__main__":
    ac = len(sys.argv)
    if ac > 1:
        if ac == 2:
            ac -= 1
            for i in sys.argv[1:]:
                print("{} argument:".format(ac))
                print("{}: {}".format(ac, i))
        elif ac > 2:
            ac -= 1
            print("{} arguments:".format(ac))
            for i, x in enumerate(sys.argv[1:], start=1):
                print("{}: {}".format(i, x))
    else:
        ac -= 1
        print("{} arguments.".format(ac))
