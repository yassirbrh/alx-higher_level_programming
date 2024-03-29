#!/usr/bin/python3

'''
    Script that takes in a URL, sends a request to the URL
    and displays the body of the response.
'''

if __name__ == "__main__":
    '''
        Importing the requests library
    '''
    import requests
    from sys import argv
    url = argv[1]
    request = requests.get(url)
    if request.status_code >= 400:
        print("Error code: {}".format(request.status_code))
    else:
        print(request.text)
