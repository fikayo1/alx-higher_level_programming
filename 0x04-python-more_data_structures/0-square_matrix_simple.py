#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for i in matrix:
        new.append([x ** 2 for x in i])
    return new
