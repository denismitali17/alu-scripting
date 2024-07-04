#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit.

    If the subreddit is invalid, return 0.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: Number of subscribers or 0 if invalid subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'CustomUserAgent/0.1'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return 0

