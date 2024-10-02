#!/usr/bin/python3
def read_file(filename=""):
    """Function for reading text file"""
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
    print(f"{read_data}")
