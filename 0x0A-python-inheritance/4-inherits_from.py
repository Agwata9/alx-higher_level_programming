#!/usr/bin/python3
# a function that returns True if the object
# a class that inherited (directly or indirectly)
# from the specified class ; otherwise False


def inherits_from(obj, a_class):
    # the object is an instance of a class that inherited
    # obj: an object
    # a_class: inherit_from

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
