#!/usr/bin/python3
""" unittest for testing the max_integer function """

import unittest
max_integer = __import__('6-max_integer').max_integer

""" Class TestMaxInteger for the test """


class TestMaxInteger(unittest.TestCase):
    """
        Initialisation of the class TestMaxInteger
    """

    def max_at_the_end(self):
        """ Max integer at the end """
        _list = [1, 3, 4, 7]
        self.assertEqual(max_integer(_list), 7)

    def max_at_the_beginning(self):
        """ Max integer at the beginning """
        _list = [22, 1, 4, 20]
        self.assertEqual(max_integer(_list), 22)

    def max_at_the_middle(self):
        """ Max integer at the middle """
        _list = [1, -2, 22, 19, 11]
        self.assertEqual(max_integer(_list), 22)

    def one_negative_in_the_list(self):
        """ One negative number in the list """
        _list = [1, -2, 22, 19, 11]
        self.assertEqual(max_integer(_list), 22)

    def only_negatives_in_the_list(self):
        """ Only negatives in the list """
        _list = [-2, -22, -20, -7]
        self.assertEqual(max_integer(_list), -2)

    def only_one_element_in_the_list(self):
        """ Only one element in the list """
        _list = [22]
        self.assertEqual(max_integer(_list), 22)

    def empty_list(self):
        """ Case of empty lists """
        _list = []
        self.assertEqual(max_integer(_list), None)
