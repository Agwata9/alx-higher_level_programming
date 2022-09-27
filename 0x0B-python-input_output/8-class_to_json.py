#!/usr/bin/python3
"""
a script that adds all arguments to a Python list
and then save them to a file:
"""


def class_to_json(obj):
    """
    a function that returns the dictionary description
    or JSON serialization of an object:
    """
    return obj.__dict__
