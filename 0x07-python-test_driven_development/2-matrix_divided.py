#!/usr/bin/python3
"""A module for dividing matrix"""


def matrix_divided(matrix, div):
    """
    a function that divides all elements in a matrix

    Args:
        matrix: a matrix of integres
        div: the number each integer in the matrix is divided by
    Returns:
        New matrix containing the divided matrix to 2 decimal place
    """
    message = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        """the matrix must be a list"""
        raise TypeError(message)
    for i in range(len(matrix)):
        c = len(matrix[i])
        if len(matrix[i]) != c:
            """each row must be the same size"""
            raise TypeError("Each row of the matrix must have the same size")
        elif type(matrix[i]) is not list:
            """Each element in the matrix must be a list"""
            raise TypeError(message)
        for each in matrix[i]:
            if type(each) not in [int, float]:
                """each element in the list of list is an integer of float"""
                raise TypeError(message)
    if type(div) not in [int, float]:
        """div must be a number"""
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    result = []
    for i in matrix:
        result.append([round(t/3, 2) for t in i])
    return result
