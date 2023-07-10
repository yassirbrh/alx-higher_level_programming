#!/usr/bin/python3
""" BaseGeometry - class """


BaseGeometry = __import__("7-base_geometry").BaseGeometry


""" Rectangle - Class inherits from BaseGeometry """

class Rectangle(BaseGeometry):
    """ Class inherits from Base BaseGeometry """

    def __init__(self, width, height):
        """ Initialisation of the constructor of the Rectangle instance """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
