#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Get to ten hot posts on a subreddit.
        Args:
            subreddit (str): queried subreddit
            """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    params = {
        "limit": 10
    }
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0" +
        "(by /u/Emergency-Jaguar3819)"
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    for c in results.get("children"):
        print(c.get("data").get("title"))
