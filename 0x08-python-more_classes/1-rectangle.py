#!/usr/bin/python3
"""Rectangle Module
"""


class Rectangle:
    """Rectangle class:
    Defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """Initializes a Rectangle Object

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.__width__ = width
        self.__height__ = height

    @property
    def width(self):
        """Getter method for width
        """
        return self.__width__

    @width.setter
    def width(self, value):
        """Setter method for width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width__ = value

    @property
    def height(self):
        """Getter method for height
        """
        return self.__height__

    @height.setter
    def height(self, value):
        """Setter method for height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height__ = value
