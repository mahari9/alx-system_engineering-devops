#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API for the subscriber count of a subreddit.

    Args:
      subreddit: The name of the subreddit to query.

    Returns:
      The number of subscribers (integer) or 0 if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "script:0x16-api_advanced:0.1 (by u/ Careful_pin_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
