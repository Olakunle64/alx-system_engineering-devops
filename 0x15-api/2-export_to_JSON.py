#!/usr/bin/python3
"""This module contains Python script that, using an API, for a given
    employee ID, export information about his/her TODO list progress
    in a json file.
    """
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    filename = f"{user_id}.json"
    todo = requests.get(
            f'https://jsonplaceholder.typicode.com/todos?userId={user_id}')
    user = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{user_id}')
    emp_name = user.json().get("username")
    todo_dict = {}
    todo_dict[str(user_id)] = []
    todo_list = todo.json()
    for each_todo in todo_list:
        small_dict = {}
        small_dict["task"] = str(each_todo["title"])
        small_dict["completed"] = str(each_todo["completed"])
        small_dict["username"] = str(emp_name)
        todo_dict[str(user_id)].append(small_dict)
    with open(filename, "w") as f:
        json.dump(todo_dict, f)
