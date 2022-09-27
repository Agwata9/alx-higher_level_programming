#!/usr/bin/python3
# Agwata ALX Cohort 7'22

class Student:
    """student class ."""

    def __init__(self, first_name, last_name, age):
        """ new Student initialization.
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """a dictionary representation of the Student."""

        return self.__dict__
