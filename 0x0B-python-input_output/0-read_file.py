#!/usr/bin/python3
"""
    A function that reads a text file with the utf-8 encoding and prints it to the stdout
"""

def read_file(filename=""):
    with open(filename, mode="r", encoding="utf-8") as myFile:
        print(myFile.read())
