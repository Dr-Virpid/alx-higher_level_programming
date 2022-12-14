#!/usr/bin/python3
"""A module containing Square Class"""


class Square:
    """A class for creating a mathematical Square"""

    def __init__(self, size=0):
        """Instantiate a Square object"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
