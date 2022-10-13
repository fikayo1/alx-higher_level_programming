#!/usr/bin/python3
"""A magic class
   containing
   things
"""


class MagicClass():
    """a magic class from byte code"""
    def __init__(self, radius):
        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.__radius == radius

    def area(self):
        from math import pi
        return (self.__radius ** 2) * pi

    def circumference(self):
        from math import pi
        return 2 * pi * self.__radius
