#!/usr/bin/python3
''' function that returns True if the object is an instance
'''


def is_kind_of_class(obj, a_class):
    '''function: is_kind_of_class
    obj: an object
    a_class: a class
    Returns: True or False
    '''
    return isinstance(obj, a_class)
