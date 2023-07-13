#!/usr/bin/python3
'''
    Import Base
'''
from models.base import Base


class Rectangle(Base):
    '''
        Initialisation of the class Rectangle
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
            Initialisation of the constructor of the class Rectangle
        '''
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        '''
            width - getter
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
            width - setter
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''
            width - getter
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
            width - setter
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''
            x - getter
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
            x - setter
        '''
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''
            y - getter
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
            y - setter
        '''
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value