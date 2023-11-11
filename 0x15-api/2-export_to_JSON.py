#!/usr/bin/python3
"""fetch info about an employee in an api
"""

import json
import requests
import sys

base_url = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":
    user_id = sys.argv[1]
    user_url = '{}/users?id={}'.format(base_url, user_id)
    response = requests.get(user_url)
    data = response.text
    data = json.loads(data)
    user_name = data[0].get('username')
    tasks_url = '{}/todos?userId={}'.format(base_url, user_id)
    response = requests.get(tasks_url)
    tasks = response.text
    tasks = json.loads(tasks)
    dict_key = str(user_id)

    builder = {dict_key: []}
    for t in tasks:
        json_data = {
            "task": t['title'],  # or use get method
            "completed": t['completed'],
            "username": user_name
        }
        builder[dict_key].append(json_data)
    json_encoded_data = json.dumps(builder)
    with open('{}.json'.format(user_id), 'w', encoding='UTF8') as myFile:
        myFile.write(json_encoded_data)
