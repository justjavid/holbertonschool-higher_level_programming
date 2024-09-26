#!/usr/bin/python3
"""Module containing BaseGeometry class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle inherit from BaseGeometry"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        Rectangle.integer_validator(self, width, self.__width)
        Rectangle.integer_validator(self, height, self.__height)
