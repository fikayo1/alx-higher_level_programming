#!/usr/bin/python3
"""2-rectange module"""


class Rectangle:
    """A class that defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Constructor for the class"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
    
    def __str__(self):
        total = ""
        if self.__height == 0 or self.__width == 0:
            return total
        else:
            for i in range(self.__height):
                total += (str(Rectangle.print_symbol) * self.__width)
                if i is not self.__height - 1:
                    total += "\n"
        return total
    
    def __del__(self):
        """print when an instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
    
    def __repr__(self):
        """string representation to create new instance"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

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
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)
