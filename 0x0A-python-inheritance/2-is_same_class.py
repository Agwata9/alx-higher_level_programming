#!/usr/bin/python3
"""a function that returns True if the object is exactly
an instance of the specified class ; otherwise False
"""

def is_same_class(obj, a_class):
    """
    is_same_class: function
    Returns:
    true if instance is exaxtly the same class otherwise returns false
    """

    if type(obj) == a_class:
        return True
    else:
        return False
