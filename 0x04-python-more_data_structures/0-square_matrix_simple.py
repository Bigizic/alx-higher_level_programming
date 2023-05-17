#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    transposed = []
    new_list = []
    for i in range(len(matrix)):
        transposed.append(matrix[i])
    for row in transposed:
        new = [num ** 2 for num in row]
        new_list.append(new)
    return new_list
