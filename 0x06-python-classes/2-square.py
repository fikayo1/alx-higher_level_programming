#!/usr/bin/python3
"""A square class"""


class Square():
    """A class that has size as a private attribute"""


    def __init__(self, size=0):
        """Constructor of a square with size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
