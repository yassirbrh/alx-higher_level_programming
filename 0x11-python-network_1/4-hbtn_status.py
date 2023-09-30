#!/usr/bin/python3

'''
    Script that fetches https://alx-intranet.hbtn.io/status
'''

if __name__ == "__main__":
    '''
        Importing the requests library
    '''
    import requests
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    if response.status_code == 200:
        print("Body response:")
        print("\t- type: {}".format(type(response.text)))
        print("\t- content: {}".format(response.text))
