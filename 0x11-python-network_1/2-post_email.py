#!/usr/bin/python3

'''
    Script that takes in a URL and an email
    sends a POST request to the passed URL with the email as a parameter
    and displays the body of the response (decoded in utf-8)
'''

if __name__ == "__main__":
    '''
        Importing the urllib library and sys.argv
    '''
    import urllib.request
    import urllib.parse
    from sys import argv
    data = {'email': argv[2]}
    data = urllib.parse.urlencode(data)
    data = data.encode('utf-8')
    request = urllib.request.Request(argv[1], data, method="POST")
    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
