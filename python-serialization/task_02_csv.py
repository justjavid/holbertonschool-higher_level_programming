#!/usr/bin/python3
"""Module for converting data from csv type to JSON type"""
import csv
import json


def convert_csv_to_json(filename):
    """Function to read csv file and convert it to JSON"""
    try:
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            data = list(reader)

        with open('data.json', 'w') as f:
                json.dump(data, file, indent=4)
                return True
    except Exception:
        return False
