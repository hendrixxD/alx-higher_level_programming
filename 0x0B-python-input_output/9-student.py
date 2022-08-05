#!/usr/bin/python3
"""defines a module that defines a class to JSON"""


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

    def to_json(self):
        """retrieves a dict repr of a student instance"""

        return self.__dict__
