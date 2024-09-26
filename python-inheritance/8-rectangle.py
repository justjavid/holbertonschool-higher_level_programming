#!/usr/bin/python3
"""Module containing BaseGeometry class"""


class BaseGeometry:
    """Class BaseGeometry"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("%s must be an integer" % (name))
        if value <= 0:
            raise ValueError("%s must be greater than 0" % (name))

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        Rectangle.integer_validator(self.__width, width)
        Rectangle.integer_validator(self.__height, height)
        self.__width = width
        self.__height = height
