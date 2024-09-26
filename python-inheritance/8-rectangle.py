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

r = Rectangle(3, 5)

print(r)
print(dir(r))

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))