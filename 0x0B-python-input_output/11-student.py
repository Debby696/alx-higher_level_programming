#!/usr/bin/python3
"""a class Student that defines a student by: (based on 10-student.py"""


class Student:
    """This represent a student."""

    def __init__(self, first_name, last_name, age):
        """This initializes a new Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """This gets a dictionary representation of the Student.
        If attrs is a list of strings, represents only those attributes
        included in the list
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """All attributes of the Student are replaced
        """
        for k, v in json.items():
            setattr(self, k, v)
