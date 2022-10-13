#!/usr/bin/python3
"""A square class"""


class Square():
    """A class with size, area method and getters & setters"""

    def __init__(self, size=0):
        """Constructor of a square with size"""
        self.size = size

    @property
    def size(self):
        """getter for private attribute size"""
        return self.__size

    @size.setter
    def size(self, size):
        """setter for provate attribute size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """calculate the area of the square with the size"""
        return self.__size*self.__size
