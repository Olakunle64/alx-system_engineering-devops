#!/usr/bin/python3
""" This module contains a function that queries the Reddit API and
    prints the titles of the first 10 hot posts listed for a given
    subreddit.
"""
import requests


def top_ten(subreddit):
    """queries the Reddit API

        Args:
            subreddit: a string

        Return: return the number of subreddit
    """
    url = "https://www.reddit.com/r/" + subreddit + "/new.json?limit=10"
    header = {"User-Agent": "Chrome/97.0.4692.71"}
    r = requests.get(url, headers=header, allow_redirects=False)
    if r.status_code != 200:
        print(None)
    try:
        subreddit_info = r.json().get("data", {})
        posts = subreddit_info.get("children", [])
        for post in posts:
            post_title = post.get("data").get("title")
            print(post_title)
    except json.decoder.JSONDecodeError:
        None
