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

    def area(self):
        """ Initialisation of the function area """
        return self.__size ** 2

    @property
    def size(self):
        """ Initialisation of the function getter for size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Initialisation of the function setter for size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, square):
        """ Define the == comparaison function to a Square """
        return self.area() == square.area()

    def __ne__(self, square):
        """ Define the != comparaison function to a Square. """
        return self.area() != square.area()

    def __lt__(self, square):
        """ Define the < comparaison function to a Square. """
        return self.area() < square.area()

    def __le__(self, square):
        """ Define the <= comparaison function to a Square. """
        return self.area() <= square.area()

    def __gt__(self, square):
        """ Define the > comparaison function to a Square. """
        return self.area() > square.area()

    def __ge__(self, square):
        """ Define the >= comparaison function to a Square. """
        return self.area() >= square.area()
