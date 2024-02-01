#!/usr/bin/python3
"""This module contains Python script that, using an API, for a given
    employee ID, returns information about his/her TODO list progress.
    """
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    todo = requests.get(
            f'https://jsonplaceholder.typicode.com/todos?userId={user_id}')
    user = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{user_id}')
    emp_name = user.json().get("name")
    done_task = 0
    t_task = 0
    undone_task = []
    todo_list = todo.json()
    for each_todo in todo_list:
        t_task += 1
        if each_todo["completed"]:
            done_task += 1
            undone_task.append(each_todo["title"])
    print(f'Employee {emp_name} is done with tasks({done_task}/{t_task}):')
    for each_todo in undone_task:
        print(f"\t {each_todo}")
