#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    names = dir()
    for name in names:
        if name[0] != '_':
            print(name)
