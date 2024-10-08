#!/usr/bin/python3
"""Module for file"""
import json


def save_to_json_file(my_obj, filename):
    """Function for saving my_obj as JSON string to file"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)

