#!/usr/bin/python3
"""
    A class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
"""


class Rectangle(BaseGeometry):
    """ Represent the rectangle width and height and validate them"""

    def __init__(self, width, height):
        """Instantiation with width and height: """
        self.width = width
        self.height = height
        self.interger_validator("width", width)
        self.interger_validator("height", height)
