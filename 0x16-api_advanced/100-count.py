#!/usr/bin/python3
""" This module contains a recursive function that queries the Reddit
    API, parses the title of all hot articles, and prints a sorted count
    of given keywords (case-insensitive, delimited by spaces.
    Javascript should count as javascript, but java should not).
"""
import requests


def sub_count_words(subreddit, word_list, word_count, after=""):
    """queries the Reddit API

        Args:
            subreddit: a string
            word_list: a list
            word_count: a dict
            after: a string

        Return: void
    """
    if after:
        url = "https://www.reddit.com/r/{}/new.json?after={}".format(
                subreddit, after)
    else:
        url = "https://www.reddit.com/r/{}/new.json".format(subreddit)
    header = {"User-Agent": "Chrome/97.0.4692.71"}
    r = requests.get(url, headers=header, allow_redirects=False)
    if r.status_code == 200:
        subreddit_info = r.json().get("data", {})
        after = subreddit_info.get("after")
        posts = subreddit_info.get("children", [])
        for post in posts:
            post_title = post.get("data").get("title")
            # print(post_title)
            for word in word_count.keys():
                if word.lower() in post_title.lower():
                    word_count[word] += 1
        if not after:
            return word_count
        else:
            # print(word_count)
            return (sub_count_words(subreddit, word_list, word_count, after))
    else:
        return None


def count_words(subreddit, word_list):
    """return the word counts"""
    unique_word_list = list(set(word_list))
    values = [0] * len(word_list)
    word_count = dict(zip(unique_word_list, values))
    # print(word_count)
    word_count_dict = sub_count_words(
            subreddit, word_list, word_count, after="")
    if word_count_dict:
        sorted_word = sorted(
                word_count_dict.items(), key=lambda item: (-item[1], item[0]))
        for item in sorted_word:
            if item[1]:
                print("{}: {}".format(item[0].lower(), item[1]))
    else:
        pass
