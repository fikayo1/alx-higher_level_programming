#!/usr/bin/python3
"""A module to add two numbers"""


def add_integer(a, b=98):
    """A function that adds 2 integers
    Args:
        a: first integer
        b: Second integer
    Returns:
        additon of two integers
    """
    if type(a) is not int or type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int or type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
