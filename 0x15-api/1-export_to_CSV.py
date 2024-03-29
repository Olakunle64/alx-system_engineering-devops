#!/usr/bin/python3
"""This module contains Python script that, using an API, for a given
    employee ID, export information about his/her TODO list progress
    to a csv file.
    """
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    csv_filename = f'{user_id}.csv'
    todo = requests.get(
            f'https://jsonplaceholder.typicode.com/todos?userId={user_id}')
    user = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{user_id}')
    USERNAME = user.json().get("username")
    full_csv_list = []
    for each_todo in todo.json():
        COMP_STATUS = each_todo.get("completed")
        TITLE = each_todo.get("title")
        # user_id = user.get("userId")
        data = f"\"{user_id}\",\"{USERNAME}\",\"{COMP_STATUS}\",\"{TITLE}\"\n"
        full_csv_list.append(data)
    with open(csv_filename, 'w', encoding="utf-8") as f:
        for data in full_csv_list:
            f.write(data)
