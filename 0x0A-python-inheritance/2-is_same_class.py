#!/usr/bin/python3
"""
is_same_class function module
"""


def is_same_class(obj, a_class):
    """function that checks if an object is an instance of a class

    Args:
        obj: object instance
        a_class: class to check

    Return:
        True if obj is an instance of a_class or False otherwise
    """
    return type(obj) is a_class  # isinstance might bring up a bug
