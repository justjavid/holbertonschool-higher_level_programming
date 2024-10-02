#!/usr/bin/python3
"""Module for writing file"""


def append_write(filename="", text=""):
    """Function for appending string
     to the end of the file"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
