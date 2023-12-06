#!/usr/bin/python3
"""
    Write a function that writes a string to a text file (UTF8) and returns 
    the number of characters written:
"""


def write_file(filename="", text=""):
    """Writes text to a file"""
    with open(filename, "w") as myFile:
        myFile.write(text)
