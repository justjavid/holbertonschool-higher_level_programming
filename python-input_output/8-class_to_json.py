#!/usr/bin/python3
"""Module for file"""
import json


def class_to_json(obj):
    """Function convert JSON str to dict"""
    return json.loads(json.dumps(obj.__dict__))
