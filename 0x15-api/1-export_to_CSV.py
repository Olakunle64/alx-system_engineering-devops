#!/usr/bin/python3
"""This module contains Python script that, using an API, for a given
    employee ID, export information about his/her TODO list progress
    to a csv file.
    """

import requests
import csv
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    todo = requests.get(
            f'https://jsonplaceholder.typicode.com/todos?userId={user_id}')
    user = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{user_id}')
    emp_name = user.json().get("name")
    user_id = user.json().get("id")

    todo_list = todo.json()

    # Specify the CSV file name
    csv_filename = f'{user_id}.csv'

    # Open the CSV file in write mode
    with open(csv_filename, 'w', newline='') as csvfile:
        # Create a CSV writer object
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        # Write the data to the CSV file
        for task in todo_list:
            task_completed_status = str(task["completed"])
            task_title = task["title"]

            csv_writer.writerow(
                    [user_id, emp_name, task_completed_status, task_title])

    # print(f'Data has been written to {csv_filename}.')
