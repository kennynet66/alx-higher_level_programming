#!/usr/bin/python3
"""
    A class Square that inherits from Rectangle (9-rectangle.py):
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ The square class that calculates the area of a square"""
    def __init__(self, size):
        """Validate the size of the square"""
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """Get the area of the square"""
        return self.__size * self.__size
