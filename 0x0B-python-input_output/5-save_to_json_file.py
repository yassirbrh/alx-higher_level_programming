#!/usr/bin/python3
""" Import JSON """
import json


def save_to_json_file(my_obj, filename):
    """ Initialisation of the function """
    text = json.dumps(my_obj)
    with open(filename, "w") as f:
        f.write(text)
