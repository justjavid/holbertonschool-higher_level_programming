#!/usr/bin/python3
"""Module containing print_sorted func"""


class MyList(list):
    """Class inherited from list class"""

    def print_sorted(self):
        print(sorted(self))
