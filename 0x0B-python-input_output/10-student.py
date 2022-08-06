#!/usr/bin/python3
"""defines a module that defines a class student to JSON with filter"""


class Student:
    """student to JSON"""

    def __init__(self, first_name, last_name, age):
        """Constructor:
        Artt: first_name
            last_name
            age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dict repr of a student instance"""

        if attrs is None:
            return self.__dict__
        return {key: value for key, value in self.__dict__.items()
                if key in attrs}
