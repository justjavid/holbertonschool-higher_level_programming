#!/usr/bin/python3
"""Module containing BaseGeometry class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class inherit from Rectangle class"""
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", self.__size)

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
