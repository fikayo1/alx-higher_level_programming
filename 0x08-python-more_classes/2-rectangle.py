#!/usr/bin/python3
"""2-rectange module"""


class Rectangle:
    """A class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Constructor for the class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for the private attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for private attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for private attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for private attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area of the triangle"""
        return self.__width * self.__height

    def perimeter(self):
        """return the perimeter of the rectangle"""
        return (2 * self.__width) + (2 * self.__height)
