#!/usr/bin/python3
"""Using RestAPI"""
import requests as req
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    usr_id = req.get(url + 'users/{}'.format(sys.argv[1])).json()
    to_do = req.get(url + 'todos', params={'userId': sys.argv[1]}).json()

    completed = [title.get("title") for title in to_do if
                 title.get('completed') is True]

    print("Employee {} is done with tasks({}/{}):".format(usr_id.get("name"),
                                                          len(completed),
                                                          len(to_do)))

    [print("\t {}".format(title)) for title in completed]
