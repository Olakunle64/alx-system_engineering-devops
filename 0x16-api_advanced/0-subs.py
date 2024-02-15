#!/usr/bin/python3
""" This module contains a function that queries the Reddit API and
    returns the number of subscribers (not active users, total
    subscribers) for a given subreddit. If an invalid subreddit is
    given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number
    of subscribers (not active users, total subscribers)
    for a given subreddit. If an invalid subreddit is given,
    the function returns 0.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit,
        or 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom User Agent"}  # Set a custom User-Agent
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        except KeyError:
            # Subscribers data not found in response JSON
            return 0
    else:
        # Subreddit not found or other error occurred
        return 0
