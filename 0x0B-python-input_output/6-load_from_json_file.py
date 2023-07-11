#!/usr/bin/python3
""" Import json """
import json


def load_from_json_file(filename):
    """ Initialisation of the function """
    with open(filename, "r") as f:
        return json.load(f)
