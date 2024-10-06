#!/usr/bin/python3
"""Module for serializing Python object to JSON file and inverse process"""
import json


def serialize_and_save_to_file(data, filename):
    """Function for saving data as JSON string to file"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Function that deserialize JSON file"""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
