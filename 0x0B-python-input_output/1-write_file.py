#!/usr/bin/python3
"""
    Write a function that writes a string to a text file (UTF8) and returns 
    the number of characters written:
"""


def write_file(filename="", text=""):
    """Writes text to a file
    Args:
        filename: Contains the name of the file to be written
        text: The text top be written to the file
    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        myFile.write(text)
