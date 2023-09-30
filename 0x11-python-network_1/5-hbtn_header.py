#!/usr/bin/python3

'''
    Script that takes in a URL, sends a request to the URL
    and displays the value of the variable X-Request-Id in the response header
'''

if __name__ == "__main__":
    '''
        Importing the urllib library and sys.argv
    '''
    import requests
    from sys import argv
    request = requests.get(argv[1])
    print(request.headers.get('X-Request-Id'))
