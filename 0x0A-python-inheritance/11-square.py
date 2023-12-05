#!/usr/bin/python3
"""
    A class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class square that inherits from the class Rectangle"""
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__size) + "/" + str(self.__size)
        return string

