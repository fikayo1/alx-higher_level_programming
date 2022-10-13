#!/usr/bin/python3
"""A square class"""


class Square():
    """A class with size, area method and getters & setters"""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor of a square with size"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """getter for private attribute position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter for private attribute position"""
        if type(value) is not tuple or len(value) != 2 \
                or type(value[0]) is not int \
                or type(value[1]) is not int \
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """calculate the area of the square with the size"""
        return self.__size*self.__size

    def my_print(self):
        """prints the square with # character and spaces"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                for j in range(self.__size):
                    if j < self.__size - 1:
                        print("#", end='')
                    else:
                        print("#")
