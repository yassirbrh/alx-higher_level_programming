#!/usr/bin/python3

""" Rectangle - Class """


class Rectangle:

    """ Initialisation of the class Rectangle """
    __width = None
    __height = None
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initialisation of the constructor of the class Rectangle """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Initialisation of the getter of the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Initialisation of the setter of the width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Initialisation of the getter of the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Initialisation of the setter of the height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Initialisation of the function area """
        return self.__height * self.__width

    def perimeter(self):
        """ Initialisation of the function perimeter """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2

    def __str__(self):
        """ Making the object printable """
        if self.__height == 0 or self.__width == 0:
            return ""
        rect = []
        for i in range(self.__height):
            string = ""
            for j in range(self.__width):
                string += str(self.print_symbol)
            rect.append(string)
        return '\n'.join(rect)

    def __repr__(self):
        """ Create a representation of the instance of the class """
        return f"Rectangle({str(self.__width)}, {str(self.__height)})"

    def __del__(self):
        """ Do some tasks after the instance of the class is deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Static method to compare two rectangles based on areas """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ method to return instance with width and height equal to size """
        return Rectangle(size, size)
