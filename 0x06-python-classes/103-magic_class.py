#!/usr/bin/python3
"""A magic class
   containing
   things
"""
from math import pi


class MagicClass():
    """a magic class from byte code"""

    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.__radius == radius

    def area(self):
        return (self.__radius ** 2) * pi

    def circumference(self):
        return 2 * pi * self.__radius
