#!/usr/bin/python3
"""
Module to query Reddit API and print titles of the first 10 hot posts
for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.

    Args:
        subreddit (str): The subreddit to query.

    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Python/requests:top_ten:v1.0.0 (by /u/yourusername)'}
    params = {'limit': 10}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)

# Example usage:
# top_ten('python')  # For an existing subreddit
# top_ten('nonexistentsubreddit')  # For a non-existent subreddit

