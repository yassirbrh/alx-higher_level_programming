#!/usr/bin/python3
"""
Import Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


"""
Square - Class
"""


class Square(Rectangle):
    """ Square - Class """
    def __init__(self, size):
        """ Initialisation of the constructor of the class Square """
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        string = "[Square] " + str(self.__size) + "/" + str(self.__size)
        return string
