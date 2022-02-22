#!/usr/bin/python3
""" queries the Reddit API and returns the number of subscribers
 (not active users, total subscribers) for a given subreddit."""

import requests

def number_of_subscribers(subreddit):
    """queries the Reddit API and returns the number of subscribers"""
    response = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "MyPythonScript"})
    if response.status_code >= 300:
        return 0

    return response.json().get("data").get("subscribers")
