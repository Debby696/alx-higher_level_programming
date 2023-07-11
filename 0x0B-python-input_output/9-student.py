#!/usr/bin/python3
"""This module defines a class Student by public instance attributes"""


class Student:
    """This represent a student."""

    def __init__(self, first_name, last_name, age):
        """A new Student is initialized
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """This gets a dictionary representation of the Student"""
        return self.__dict__
