#!/usr/bin/python3
"""
    A class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
"""
BaseGeometry = __import__('7-base-geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Represent the rectangle width and height and validate them"""

    def __init__(self, width, height):
        """Instantiation with width and height: """
        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
        self.integer_validator("height", height)
