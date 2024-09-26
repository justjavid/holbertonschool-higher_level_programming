#!/usr/bin/python3
"""Module containing BaseGeometry class"""


class BaseGeometry:
    """Class BaseGeometry"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value, int) is False:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
