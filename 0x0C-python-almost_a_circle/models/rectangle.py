#!/usr/bin/python3
"""class module"""
from base import Base


class Rectangle(Base):
    """A class that inherits from the base class"""

    def __init__(self, width, height, x=0, y=0, id=None):

        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y


    @property
    def width(self):
        """getter for the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 1:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
       """getter for the height"""
       return self.__height

    @height.setter
    def height(self, value):
        """setter for the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 1:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for the x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for the x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for the x"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for the y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.height * self.width

    def display(self):
        for i in range(self.height):
            print("#" * self.width)
