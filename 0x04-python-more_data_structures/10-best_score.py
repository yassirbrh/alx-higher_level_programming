#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        bg_score = None
        name = ""
        for key in a_dictionary:
            if bg_score < a_dictionary[key]:
                bg_score = a_dictionary[key]
                name = key
        return name
