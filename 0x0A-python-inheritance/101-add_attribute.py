#!/usr/bin/python3
"""
    A function that adds a new attribute to an object if it is possible:
"""


def add_attribute(obj, attr, value):
    """
        Raise a TypeError exception, with the message can't add new attribute
        if the object cannott have new attribute
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
