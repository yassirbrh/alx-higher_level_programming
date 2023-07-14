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

    def area(self):
        '''
            area - Instance method to calculate the rectangle area
        '''
        return self.__width * self.__height

    def display(self):
        '''
            display - Instance method to print the rectangle using #
        '''
        for i in range(self.y):
            print("")
        for i in range(self.height):
            for j in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        '''
            Function to transform the object into printable format
        '''
        string = "[Rectangle] (" + str(self.id) + ") "
        string += str(self.x) + "/" + str(self.y) + " - "
        string += str(self.width) + "/" + str(self.height)
        return string

    def update(self, *args, **kwargs):
        '''
            Function to update the object properties
        '''
        if args is not None and len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for kwarg in kwargs:
                if kwarg == "id":
                    self.id = kwargs[kwarg]
                if kwarg == "width":
                    self.width = kwargs[kwarg]
                if kwarg == "height":
                    self.height = kwargs[kwarg]
                if kwarg == "x":
                    self.x = kwargs[kwarg]
                if kwarg == "y":
                    self.y = kwargs[kwarg]

    def to_dictionary(self):
        '''
            Initialisation of the instance method to_dictionary
        '''
        to_dict = {"x": self.x, "y": self.y, "id": self.id}
        to_dict["height"] = self.height
        to_dict["width"] = self.width
        return to_dict
