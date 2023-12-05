#!/usr/bin/python3
"""
    A class MyList that inherits from list
"""


class MyList(list):
    """A class MyList that has a public function that sorts in ascending order"""

    def print_sorted(self):
        """ Sorts a list in ascending order."""
        print(sorted(self))
