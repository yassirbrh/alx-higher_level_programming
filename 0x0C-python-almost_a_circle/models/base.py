#!/usr/bin/python3
'''
    Import JSON
'''
import json

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

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
            to_json_string - Static method to return the json format of dicts
        '''
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
