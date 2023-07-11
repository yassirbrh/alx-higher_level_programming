#!/usr/bin/python3
'''
    Student - Class
'''


class Student:
    '''
        Initialisation of the class Student
    '''
    def __init__(self, first_name, last_name, age):
        '''
            Initialisation of the constructor of the class Student
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
            to_json - Function
        '''
        if attrs is not None and type(attrs) == list:
            dict_attrs = dict()
            for attr in attrs:
                if attr in vars(self):
                    dict_attrs[attr] = vars(self)[attr]
            return dict_attrs
        return vars(self)
