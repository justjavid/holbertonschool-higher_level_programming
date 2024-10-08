#!/usr/bin/python3
"""Module for class"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        new_dict = {}
        if attrs is None:
            return self.__dict__
        for key in attrs:
            if key in self.__dict__.keys():
                new_dict[key] = self.__dict__[key]
        return new_dict
