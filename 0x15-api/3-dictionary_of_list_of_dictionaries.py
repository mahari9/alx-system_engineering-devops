#!/usr/bin/python3
"""Script to export data in the JSON format.
   Format: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
  "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task":
  "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID":
  [ {"username": "USERNAME", "task": "TASK_TITLE", "completed":
  TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE",
  "completed": TASK_COMPLETED_STATUS}, ... ]}
   File name: todo_all_employees.json
"""

import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(url + "todos",
                                    params={"userId": u.get("id")}).json()]
            for u in users}, jsonfile)
