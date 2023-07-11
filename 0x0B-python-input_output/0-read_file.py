#!/usr/bin/python3


""" read_file - Function """


def read_file(filename=""):
    """ Initialisation of the function read_file """
    with open(filename, "r", encoding="UTF-8") as f:
        for line in f:
            print(line, end="")
