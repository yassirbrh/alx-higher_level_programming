#!/usr/bin/python3

'''
    Script that takes in a URL, sends a request to the URL
    and displays the body of the response (decoded in utf-8).
'''

if __name__ == "__main__":
    '''
        Importing the urllib library and sys.argv
    '''
    import urllib.request
    import urllib.parse
    from sys import argv
    try:
        request = urllib.request.Request(argv[1])
        with urllib.request.urlopen(request) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
