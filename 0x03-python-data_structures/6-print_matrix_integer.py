#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for i, n in enumerate(x):
            if i == len(x) - 1:
                print("{:d}".format(n), end="")
            else:
                print("{:d}".format(n), end=" ")
        print()
