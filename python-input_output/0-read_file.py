#!/usr/bin/python3
"""Function for reading text file"""
def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
    print(f"{read_data}")
