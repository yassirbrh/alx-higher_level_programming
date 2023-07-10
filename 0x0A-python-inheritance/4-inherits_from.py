#!/usr/bin/python3
""" inherits_from - Function """


def inherits_from(obj, a_class):
    """ Function to check if an object inherits from a specific class """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
