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

    @classmethod
    def save_to_file(cls, list_objs):
        '''
            save_to_file - Class method to save the json format in a file
        '''
        list_dict = []
        for obj in list_objs:
            list_dict.append(obj.to_dictionary())
        content = Base.to_json_string(list_dict)
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(content)

    @staticmethod
    def from_json_string(json_string):
        '''
            from_json_string - Method to extract the list of dicts from json.
        '''
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
            create - Class method to create an instance of the class
        '''
        if dictionary is not None and len(dictionary) != 0:
            if cls.__name__ == "Square":
                obj = cls(11)
            else:
                obj = cls(22, 11)
            obj.update(**dictionary)
            return obj
