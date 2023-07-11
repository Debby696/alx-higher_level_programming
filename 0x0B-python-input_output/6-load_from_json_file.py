#!/usr/bin/python3
"""This defines the creation of a python object from a JSON file"""
import json


def load_from_json_file(filename):
    """A function that creates a Python object from a given JSON file"""
    with open(filename) as f:
        return json.load(f)
