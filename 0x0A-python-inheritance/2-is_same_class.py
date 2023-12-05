#!/usr/bin/python3
"""A function that returns True if the object is exactly an instance of the specified class ; otherwise False"""


def is_same_class(obj, a_class):
    """Checks if the object is an instance of an existing class"""

    if type(obj) is a_class:
        return True
    return False
