#!/usr/bin/python3
"""This module defines a file-writing function using JSON format"""
import json


def save_to_json_file(my_obj, filename):
    """A function that Writes an object to a text file using JSON format"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
