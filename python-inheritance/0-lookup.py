#!/usr/bin/python3
"""Module for look up attributes of class"""


def lookup(obj):
    """Function for list all attributes"""
    return list(dir(obj))
