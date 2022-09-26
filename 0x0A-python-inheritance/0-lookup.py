#!/usr/bin/python3
"""
a function that returns the list of available attributes and methods of an object:
"""

def lookup(obj):
    """ function: lookup()
    obj: variable to be looked by the function
    """

    return dir(obj)
