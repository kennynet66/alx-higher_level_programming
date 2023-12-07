#!/usr/bin/python3
"""
    Write a function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added:
"""


def append_write(filename="", text=""):
    """ appends a string at the end of a text file
    Args:
        filename - The name of the file to be appended
        text - The text to be appended
    """

    with open(filename, "a", encoding="utf-8") as myFile:
        return myFile.write(text)
