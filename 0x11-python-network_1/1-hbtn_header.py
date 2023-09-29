#!/usr/bin/python3

'''
    Script that takes in a URL, sends a request to the URL
    and displays the value of the X-Request-Id variable
'''

if __name__ == "__main__":
    '''
        Importing the urllib library and sys.argv
    '''
    import urllib.request
    from sys import argv
    request = urllib.request.Request(argv[1])
    with urllib.request.urlopen(argv[1]) as response:
        print(dict(response.headers)['X-Request-Id'])
