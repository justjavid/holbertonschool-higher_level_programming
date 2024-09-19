#!/usr/bin/python3
"""Module for creating empty class"""


class Square:
    """Create a private attribute and using getter and setter"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if not self.__size:
            print()
        for i in range(self.__size):
            print(self.__size * "#")
