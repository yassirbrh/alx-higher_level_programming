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

    def __str__(self):
        '''
            Making the square object printable
        '''
        string = "[Square] (" + str(self.id) + ") "
        string += str(self.x) + "/" + str(self.y) + " - "
        string += str(self.width)
        return string
