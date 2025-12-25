#!/usr/bin/python3
"""Fuckass module"""

class MyList(list):
    """MyList class inherits from list"""

    @instancemethod
    def print_sorted(self):
        """Prints the list in ascending order"""
        print(sorted(self))