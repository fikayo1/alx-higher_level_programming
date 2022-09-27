#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for list in matrix:
            for element in list:
                print("{:d}".format(element), end=" ")
            if matrix.index(list) != len(matrix) - 1:
                print()
