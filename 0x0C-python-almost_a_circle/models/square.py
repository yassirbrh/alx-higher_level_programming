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

    @property
    def size(self):
        '''
            Initialisation of the size getter
        '''
        return self.width

    @size.setter
    def size(self, value):
        '''
            Initialisation of the size setter
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        '''
            Making the square object printable
        '''
        string = "[Square] (" + str(self.id) + ") "
        string += str(self.x) + "/" + str(self.y) + " - "
        string += str(self.width)
        return string

    def update(self, *args, **kwargs):
        '''
            Initialisation of the instance method update
        '''
        if args is not None and len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for kwarg in kwargs:
                if kwarg == "id":
                    self.id = kwargs[kwarg]
                if kwarg == "size":
                    self.size = kwargs[kwarg]
                if kwarg == "x":
                    self.x = kwargs[kwarg]
                if kwarg == "y":
                    self.y = kwargs[kwarg]
