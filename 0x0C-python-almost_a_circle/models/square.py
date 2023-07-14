#!/usr/bin/python3
'''
    Import Rectangle to square inherits from
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''
        Square - Class that inherits from Rectangle class
    '''

    def __init__(self, size, x=0, y=0, id=None):
        '''
            Initialisation of the constructor of the class Square
        '''
        super().__init__(size, size, x, y, id)
        self.__size = size

    @property
    def size(self):
        '''
            Initialisation of the size getter
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
            Initialisation of the size setter
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value

    def __str__(self):
        '''
            Making the square object printable
        '''
        string = "[Square] (" + str(self.id) + ") "
        string += str(self.x) + "/" + str(self.y) + " - "
        string += str(self.width)
        return string
