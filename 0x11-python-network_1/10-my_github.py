#!/usr/bin/python3

'''
    Script that takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id.
'''

if __name__ == "__main__":
    '''
        Importing the requests library
    '''
    import requests
    from requests.auth import HTTPBasicAuth
    from sys import argv
    url = 'https://api.github.com/user/{}'.format(argv[1])
    request = requests.get(url, auth=HTTPBasicAuth(argv[1], argv[2]))
    print(request.json().get('id'))
