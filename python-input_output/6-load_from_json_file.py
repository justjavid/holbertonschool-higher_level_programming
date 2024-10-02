#!/usr/bin/python3
"""Module for file"""
import json


def load_from_json_file(filename):
    """Function that creates object from JSON file"""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
