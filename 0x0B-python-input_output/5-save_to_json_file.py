#!/usr/bin/python3
""" Import JSON """
import json


""" save_to_json_file - Function """


def save_to_json_file(my_obj, filename):
    """ Initialisation of the function """
    text = json.dumps(my_obj)
    with open(filename, "w") as f:
        f.write(text)
