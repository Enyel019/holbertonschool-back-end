#!/usr/bin/python3
"""Gather data from an API."""

import requests
import sys

if __name__ == '__main__':

    api_url = 'https://jsonplaceholder.typicode.com'
    employee_id = sys.argv[1]

    employee_url = f'{api_url}/users/{employee_id}'
    response = requests.get(employee_url)
    employee_data = response.json()
    employee_name = employee_data['name']

    todos_url = f'{api_url}/users/{employee_id}/todos'
    response = requests.get(todos_url)
    todos_data = response.json()

    completed_tasks = 0
    total_tasks = len(todos_data)

    completed_titles = []

    for todo in todos_data:
        if todo['completed']:
            completed_tasks += 1
            completed_titles.append(todo['title'])

    print(f"Employee {employee_name} is done with tasks({completed_tasks}/\
        {total_tasks}):")
    for title in completed_titles:
        print(f"\t{title}")
