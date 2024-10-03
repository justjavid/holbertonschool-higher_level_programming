#!/usr/bin/python3
"""Module for file"""


def class_to_json(obj):
    """Function convert JSON str to dict"""
    return obj.__dict__
