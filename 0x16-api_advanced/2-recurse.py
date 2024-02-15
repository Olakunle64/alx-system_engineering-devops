#!/usr/bin/python3
""" This module contains a recursive function that queries the Reddit
    API and returns a list containing the titles of all hot articles
    for a given subreddit. If no results are found for the given
    subreddit, the function should return None.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """queries the Reddit API

        Args:
            subreddit: a string

        Return: return the number of subreddit
    """
    if after:
        url = "https://www.reddit.com/r/{}/new.json?after={}".format(
                subreddit, after)
    else:
        url = "https://www.reddit.com/r/{}/new.json".format(subreddit)
    header = {"User-Agent": "Chrome/97.0.4692.71"}
    r = requests.get(url, headers=header, allow_redirects=False)
    if r.status_code != 200:
        return None
    subreddit_info = r.json().get("data", {})
    after = subreddit_info.get("after")
    posts = subreddit_info.get("children", [])
    for post in posts:
        post_title = post.get("data").get("title")
        # print(post_title)
        hot_list.append(post_title)
    if not after:
        return hot_list
    else:
        return (recurse(subreddit, hot_list, after))
