#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    od_set = set()
    for first_item in set_1:
        for sec_item in set_2:
            if first_item not in set_2 and first_item not in od_set:
                od_set.add(first_item)
            if sec_item not in set_1 and sec_item not in od_set:
                od_set.add(sec_item)
    return od_set
