#!/usr/bin/python3
"""
lookup function module
"""


def lookup(obj):
    """Returns the list of all available attributes and methods of an object

    Args:
        obj: object

    Return:
        list of all available attributes and methods of an object
    """
    return dir(obj)
