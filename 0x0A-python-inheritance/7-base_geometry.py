#!/usr/bin/python3
"""
    A class BaseGeometry (based on 6-base_geometry.py).
"""


class BaseGeometry:
    """ The class"""

    def area(self):
        """raises an Exception with the message area() is not implemented"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value:"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
