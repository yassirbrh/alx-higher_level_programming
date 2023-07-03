#!/usr/bin/python3

""" say_my_name - Function
    @first_name: The First Name
    @last_name: The Last Name
    return: No return
"""


def say_my_name(first_name, last_name=""):
    """
        Prints 'My name is <first name> <last name>'
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
