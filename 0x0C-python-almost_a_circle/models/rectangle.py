#!/usr/bin/python3
"""
A Rectangle module
"""
from models.base import Base


class Rectangle(Base):
    """A Rectangle Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Class Instance

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int): x coordinate of rectangle
            y (int): y coordinate of rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def int_checker(name, value):
        """checks if a value meets the int requirement"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if len(name) == 1 and value < 0:
            raise ValueError(f"{name} must be >= 0")
        if value <= 0 and len(name) > 1:
            raise ValueError(f"{name} must be >= 0")

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        Rectangle.int_checker("width", value)
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """width setter"""
        Rectangle.int_checker("height", value)
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        Rectangle.int_checker("x", value)
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        Rectangle.int_checker("y", value)
        self.__y = value
