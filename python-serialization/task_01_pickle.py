#!/usr/bin/python3
"""Module for serialize and deserialize Python objects"""
import pickle


class CustomObject:
    def __init__(name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student
    
    
    def display(self):
        print(f"Name: {self.name}
                Age: {self.age}
                Is Student: {self.is_student}")
    
    def serialize(self, filename):
    """Function to serialize and save Instance to a file."""
    try:
        with open(filename, 'wb') as f:
            pickle.dump(self, f)
    except Exception:
        return None
     
      
    @classmethod deserialize(cls, filename):
        """Function to load and deserialize data from a file."""
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
