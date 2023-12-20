#!/usr/bin/python3
"""Module for task 1"""
import requests


def top_ten(subreddit):
    """Queries the Reddit API and returns the top 10 hot posts"""
    sub = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                       .format(subreddit),
                       headers={"User-Agent": "My-User-Agent"},
                       allow_redirects=False)
    if sub.status_code >= 300:
        print('None')
    else:
        [print(child.get("data").get("title"))
         for child in sub.json().get("data").get("children")]