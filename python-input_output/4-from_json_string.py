#!/usr/bin/python3
"""Module for file"""
import json


def from_json_string(my_obj):
    """Function for returning Python object representing JSON string"""
    return json.loads(my_obj)
