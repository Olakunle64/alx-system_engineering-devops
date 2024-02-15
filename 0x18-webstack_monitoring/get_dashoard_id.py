#!/usr/bin/python3

import requests

# Replace 'YOUR_API_KEY' with your Datadog API key
headers = {'DD-API-KEY': api_key, 'DD-APPLICATION-KEY': api}

# Datadog API endpoint for retrieving dashboard list
url = 'https://api.datadoghq.com/api/v1/dashboard'
# url = 'https://app.datadoghq.com/dashboard/'
# Send GET request to retrieve dashboard list
response = requests.get(url, headers=headers)

# Check if request was successful (status code 200)
if response.status_code == 200:
    # Parse response JSON
    dashboard_list = response.json()
    
    # Iterate over dashboard objects
    for dashboard in dashboard_list['dashboards']:
        dashboard_id = dashboard['id']
        dashboard_title = dashboard['title']
        print(f"Dashboard Title: {dashboard_title}, Dashboard ID: {dashboard_id}")

else:
    print(f"Error: Unable to retrieve dashboard list. Status Code: {response.status_code}")

