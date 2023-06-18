#!/usr/bin/python3
"""Gather data from an API."""

import requests
import sys
import string

if __name__ == '__main__':

    emp_id = sys.argv[1]

    api_url = "https://jsonplaceholder.typicode.com"

    url = f"{api_url}/users/{emp_id}/todos"
    resp = requests.get(url)
    emp_tasks = resp.json()

    url = f"{api_url}/users/{emp_id}"
    resp = requests.get(url)
    emp_info = resp.json()

    for task in emp_tasks:
        alphanumeric_value = ''.join(
            [char for char in string.ascii_letters + string.digits if char != emp_info["username"]]
        )

        output = "\"{}\",\"{}\",\"{}\",\"{}\"\n".format(
            emp_info.get("id"), emp_info.get("username"),
            task.get("completed"), task.get("title"))

        with open(f"{emp_id}.csv", mode="a", encoding="utf-8") as f:
            f.write(output)
