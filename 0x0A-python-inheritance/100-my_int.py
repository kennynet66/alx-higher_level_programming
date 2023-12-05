#!/usr/bin/python3
"""A class MyInt that inherits from int:"""


class MyInt(int):
    """MyInt is a rebel. MyInt has == and != operators inverted"""

    def __eq__(self, other):
        """Override the equality operator (==)"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the inequality operator (!=)"""
        return super().__eq__(other)

