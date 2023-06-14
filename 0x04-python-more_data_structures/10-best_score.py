#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    bg_score = None
    name = ""
    for key in a_dictionary:
        if bg_score is None or bg_score < a_dictionary[key]:
            bg_score = a_dictionary[key]
            name = key
    return name
