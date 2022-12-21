#!/usr/bin/python3
"""A module containing Class Square"""

class Square:
    """A class for creating a mathematical Square"""

    def __init__(self, size=0):
        """Instantiate a Square object"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    @property
    def size(self):
        """Getter for the private size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the private size attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
