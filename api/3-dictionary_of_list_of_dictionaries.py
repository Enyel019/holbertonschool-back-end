#!/usr/bin/python3
"""Gather data from an API."""

import requests
import sys
import json


def gather_data(emp_id):
    api_url = "https://jsonplaceholder.typicode.com"

    url = f"{api_url}/users/{emp_id}/todos"
    resp = requests.get(url)
    emp_tasks = resp.json()

    url = f"{api_url}/users/{emp_id}"
    resp = requests.get(url)
    emp_info = resp.json()

    emp_todos = []

    for task in emp_tasks:
        emp_todos.append({
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': emp_info.get('username')
        })

    return emp_todos


if __name__ == '__main__':
    users = [gather_data(emp_id) for emp_id in range(1, 11)]
    # Create dictionary with user IDs as keys and tasks as values
    all_users_tasks = dict(enumerate(users, start=1))

    # Save the dictionary as JSON
    with open("todo_all_employees.json", mode="w") as f:
        json.dump(all_users_tasks, f)
