#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
        Initialisation of the class TestMaxInteger
    """

    def test_max_at_the_end(self):
        """ Max integer at the end """
        test_list =[1, 3, 4, 7]
        self.assertEqual(max_integer(test_list), 7)

    def test_max_at_the_beginning(self):
        """ Max integer at the beginning """
        test_list =[22, 1, 4, 20]
        self.assertEqual(max_integer(test_list), 22)

    def test_max_at_the_middle(self):
        """ Max integer at the middle """
        test_list =[1, -2, 22, 19, 11]
        self.assertEqual(max_integer(test_list), 22)

    def test_one_negative_in_the_list(self):
        """ One negative number in the list """
        test_list =[1, -2, 22, 19, 11]
        self.assertEqual(max_integer(test_list), 22)

    def test_only_negatives_in_the_list(self):
        """ Only negatives in the list """
        test_list =[-2, -22, -20, -7]
        self.assertEqual(max_integer(test_list), -2)

    def test_only_one_element_in_the_list(self):
        """ Only one element in the list """
        test_list =[22]
        self.assertEqual(max_integer(test_list), 22)

    def test_empty_list(self):
        """ Case of empty lists """
        test_list =[]
        self.assertEqual(max_integer(test_list), None)


if __name__ == '__main__':
    unittest.main()
