#!/usr/bin/python3
"""
MyList module
"""


class MyList(list):
    """MyList class subclassed from list object"""

    def print_sorted(self):
        """Prints the list sorted in asscending order"""
        print(sorted(self))
