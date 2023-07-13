#!/usr/bin/python3

'''
    Base - Class
'''


class Base:
    '''
        Initialisation of the class Base
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''
            Initialisation of the constructor of the class Base
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
