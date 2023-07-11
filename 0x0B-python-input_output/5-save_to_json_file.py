#!/usr/bin/python3
'''
    Import JSON
'''
import json


def save_to_json_file(my_obj, filename):
    '''
        Function to write the object to a text file in JSON format
    '''
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
