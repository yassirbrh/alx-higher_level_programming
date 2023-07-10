#!/usr/bin/python3
"""
Import Rectangle
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Class Square inherits from class Rectangle """
    def __init__(self, size):
        """ Initialisation of the constructor of the class Square """
        self.__size = size
        super().__init__(self.__size, self.__size)
