#!/usr/bin/python3
""" is_same_class - Function """


def is_same_class(obj, a_class):
    """ Function to check if an object is an instance of a class """
    if type(obj) == a_class:
        return True
    return False
