#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        print()
    else:
        for list in matrix:
            for element in list:
                print("{:d}".format(element), end=" ")
            print()
