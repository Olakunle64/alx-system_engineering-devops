#!/usr/bin/python3
"""This module contains Python script that, using an API, for a given
    employee ID, export information about his/her TODO list progress
    in a json file.
    """
import json
import requests
import sys

if __name__ == "__main__":
    filename = "todo_all_employees.json"
    big_dict = {}
    users = requests.get(
            f'https://jsonplaceholder.typicode.com/users/')
    for user in users.json():
        id = str(user.get("id"))
        todo = requests.get(
                f'https://jsonplaceholder.typicode.com/todos?userId={id}')
        # print(user.text)
        emp_name = user.get("username")
        # print(emp_name)
        # id = str(user.json().get("id"))
        todo_dict = {}
        todo_dict[id] = []
        todo_list = todo.json()
        for each_todo in todo_list:
            small_dict = {}
            small_dict["task"] = str(each_todo["title"])
            small_dict["completed"] = str(each_todo["completed"])
            small_dict["username"] = str(emp_name)
            todo_dict[id].append(small_dict)
        big_dict[id] = todo_dict[id]
    with open(filename, "w") as f:
        json.dump(big_dict, f)
