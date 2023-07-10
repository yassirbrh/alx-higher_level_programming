#!/usr/bin/python3
""" BaseGeometry - class """


class BaseGeometry:
    """ Empty class BaseGeometry """
    pass

    def area(self):
        """ area - Class method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer_validator - Class method """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
