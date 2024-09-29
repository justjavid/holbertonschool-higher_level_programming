#!/usr/bin/python3
"""Module for multuiple inherit class"""


class SwimMixin:
    """SwimMixin class"""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """FlyMixin class"""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class"""
    def roar(self):
        print("The dragon roars!")
