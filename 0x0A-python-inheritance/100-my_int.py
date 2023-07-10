#!/usr/bin/python3
""" MyInt - Class"""


class MyInt(int):
    """ MyInt inherits from int """

    def __eq__(self, value):
        """ Function to override != for MyInt """
        return self.real != value

    def __ne__(self, value):
        """ Function to override == for MyInt """
        return self.real == value
