#!/usr/bin/python3
""" This module contains a function that queries the Reddit API and
    returns the number of subscribers (not active users, total
    subscribers) for a given subreddit. If an invalid subreddit is
    given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API

        Args:
            subreddit: a string

        Return: return the number of subreddit
    """
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    header = {"User-Agent": "Chrome/97.0.4692.71"}
    r = requests.get(url, headers=header, allow_redirects=False)
    if r.status_code != 200:
        return 0
    return r.json()["data"]["subscribers"]
