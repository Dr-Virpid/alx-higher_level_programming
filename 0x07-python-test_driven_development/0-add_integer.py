#!/usr/bin/python3
"""Addition of Numbers
function to add two integers
"""


def add_integer(a, b=98):
    """Adds 2 numbers together

    Args:
        a: first number
        b: second number

    Returns:
        The sum of the two numbers
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")

    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    c = int(a) + int(b)
    return c
