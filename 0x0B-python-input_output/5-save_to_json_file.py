#!/usr/bin/python
""" Import JSON """
import json


""" save_to_json_file - Function """


def save_to_json_file(my_obj, filename):
    """ Initialisation of the function """
    text = json.dump(my_obj)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
