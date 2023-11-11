#!/usr/bin/python3
"""Export data in the CSV format"""
import csv
import requests as req
import sys
import json
import re



API = "https://jsonplaceholder.typicode.com"
if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            user_res = req.get('{}/users/{}'.format(API, id)).json()

            tasks = req.get('{}/todos'.format(API)).json()
            user_name = user_res.get('username')
            tasks = list(filter(lambda x: x.get('userId') == id, tasks))

            with open('{}.csv'.format(id), 'w') as file:
                for t in tasks:
                    file.write(
                        '"{}","{}","{}","{}"\n'.format(
                            id,
                            user_name,
                            t.get('completed'),
                            t.get('title')
                        )
                    )
