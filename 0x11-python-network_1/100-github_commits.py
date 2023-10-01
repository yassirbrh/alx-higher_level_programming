#!/usr/bin/python3

'''
    Python script that takes 2 arguments in order to solve the Github challenge
'''

if __name__ == "__main__":
    '''
        Importing the requests library
        and sys.argv
    '''
    import requests
    from sys import argv
    try:
        repo = argv[1]
        usr_nm = argv[2]
        url = 'https://api.github.com/repos/{}/{}/commits'.format(usr_nm, repo)
        request = requests.get(url)
        commits = request.json()
        for i in range(10):
            print("{}: ".format(commits[i].get("sha")), end="")
            name = commits[i].get("commit").get("author").get("name")
            print("{}".format(name))
    except IndexError:
        pass
