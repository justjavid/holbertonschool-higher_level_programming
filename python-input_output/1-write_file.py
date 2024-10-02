#!/usr/bin/python3
"""Module for writing file"""


def write_file(filename="", text=""):
    """Function for writing text to file"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
