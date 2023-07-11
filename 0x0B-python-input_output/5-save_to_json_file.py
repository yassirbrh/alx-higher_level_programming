#!/usr/bin/python
""" Import JSON """
import json


""" save_to_json_file - Function """


def save_to_json_file(my_obj, filename):
    """ Initialisation of the function """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
