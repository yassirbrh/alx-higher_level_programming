#!/usr/bin/python3
""" MyList class """


class MyList(list):
    """ Class MyList inherits from list """
    def __init__(self):
        """ initialisation of the object """
        super().__init__()

    def print_sorted(self):
        """ function to prints the sorted list """
        print(sorted(self))
