#!/usr/bin/python3
"""Student to JSON."""


class Student:
    """A student class."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return the JSON representation of the student."""
        return dict(self.__dict__)
