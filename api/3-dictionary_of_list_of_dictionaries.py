#!/usr/bin/python3
"""Gather data from an API."""

import requests
import json

if __name__ == '__main__':

    api_url = "https://jsonplaceholder.typicode.com"

    url = f"{api_url}/users"
    resp = requests.get(url)
    users = resp.json()

    all_todos = {}

    for user in users:
        user_id = user['id']

        url = f"{api_url}/users/{user_id}/todos"
        resp = requests.get(url)
        todos = resp.json()

        emp_todos = [
            {
                'task': task.get('title'),
                'completed': task.get('completed'),
                'username': user.get('username'),
            }
            for task in todos
        ]
        all_todos[user_id] = emp_todos

    file_name = "todo_all_employees.json"
    with open(file_name, mode="w") as f:
        json.dump(all_todos, f)
