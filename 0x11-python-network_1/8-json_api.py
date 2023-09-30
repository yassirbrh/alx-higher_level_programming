#!/usr/bin/python3

'''
    Python script that takes in a letter
    and sends a POST request to http://0.0.0.0:5000/search_user
    with the letter as a parameter.
'''

if __name__ == "__main__":
    '''
        Importing the requests library
        and sys.argv
    '''
    import requests
    from sys import argv
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) < 2:
        q = ""
    else:
        q = argv[1]
    data = {'q': q}
    request = requests.post(url, data)
    try:
        usr_id = request.json().get("id")
        name = request.json().get("name")
        if request.json():
            print("[{}] {}".format(usr_id, name))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
