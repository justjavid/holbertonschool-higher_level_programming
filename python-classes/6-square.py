#!/usr/bin/python3
"""Module for creating empty class"""


class Square:
    """Create a private attribute and using getter and setter"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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
        if (len(value) != 2) or any(v < 0 for v in value) or any(not isinstance(v, int) for v in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if not self.__size:
            print()
        for i in range(self.__position[1]):
            print("\n" * self.__position[1], end="")
        for i in range(self.__size):
            print(self.__position[0] * " " + self.__size * "#")
