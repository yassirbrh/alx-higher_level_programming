#!/usr/bin/python3
'''
    Import SYS
'''
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


if __name__ == "__main__":
    filename = "add_item.json"
    try:
        obj = load_from_json_file(filename)
    except FileNotFoundError:
        obj = []
    for i in range(1, len(sys.argv)):
        obj.append(sys.argv[i])
    save_to_json_file(obj, filename)
