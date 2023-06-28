#!/usr/bin/python3


""" Creation of the Square class """


class Square:

    """ Definition of the Square class """
    __size = None

    def __init__(self, size=0):
        """ Initialisation of the class """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
