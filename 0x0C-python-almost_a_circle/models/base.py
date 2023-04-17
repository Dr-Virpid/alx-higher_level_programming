#!/usr/bin/python3
"""
Base class module
"""


class Base:
    """
    A Base Class with autoincrementing id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize class Base

        Args:
            id: id of Base instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
