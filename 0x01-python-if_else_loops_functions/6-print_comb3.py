#!/usr/bin/python3
for i in range(10):
    for x in range(i+1, 10):
        print("{:d}{:d}".format(i, x), end=", " if i != 8 or x != 9 else "\n")
