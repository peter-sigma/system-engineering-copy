#!/usr/bin/python3
"""fetch info about employees using an api
and exports it in json format
"""
import json
import requests


base_url = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":
    users_url = '{}/users'.format(base_url)

    response = requests.get(users_url)
    data = response.text
    data = json.loads(data)

    builder = {}
    for user in data:
        user_id = user.get('id')
        user_name = user.get('username')
        dict_key = str(user_id)

        builder[dict_key] = []
        tasks_url = '{}/todos?userId={}'.format(base_url, user_id)

        response = requests.get(tasks_url)
        tasks = response.text
        tasks = json.loads(tasks)

        for t in tasks:
            json_data = {
                "task": t['title'],  # or use get method
                "completed": t['completed'],
                "username": user_name
            }
            builder[dict_key].append(json_data)
    json_encoded_data = json.dumps(builder)
    with open('todo_all_employees.json', 'w', encoding='UTF8') as myFile:
        myFile.write(json_encoded_data)
