#!/usr/bin/python3

'''
    Script that takes in a URL and an email address
    sends a POST request to the passed URL with the email as a parameter
    and finally displays the body of the response.
'''

if __name__ == "__main__":
    '''
        Importing the requests library
    '''
    import requests
    from sys import argv
    input_data = {'email': argv[2]}
    response = requests.post(argv[1], input_data)
    print(response.text)
