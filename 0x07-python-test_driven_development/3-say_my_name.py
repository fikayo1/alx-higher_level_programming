#!/usr/bin/python3
"""3-say my name module"""


def say_my_name(first_name, last_name=""):
    """
    A function that prints My name is <first_name> <last_name>
    Args:
        first_name: The first name to be printed
        last_name: The last name to be printed
    """
    if type(first_name) is not str:
        return TypeError("first_name must be a string")
    elif type(last_name) is not str:
        return TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
