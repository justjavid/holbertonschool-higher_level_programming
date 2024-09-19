#!/usr/bin/python3
"""Module for creating empty class"""


class Square:
    """Create a private attribute and using getter and setter"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if not (isinstance(all(value), int) and isinstance(value, tuple)) or all(value) < 0 or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if not self.__size:
            print()
        for i in range(self.__position[1]):
            print("\n" * self.__position[1], end="")
        for i in range(self.__size):
            print(self.__position[0] * " ", end="")
            print(self.__size * "#")
