#!/usr/bin/python3

""" add_attribute - Function """


def add_attribute(obj, attr, value):
    """ Initialisation of the function add_attribute """
    if type(obj).__module__ == "builtins":
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
