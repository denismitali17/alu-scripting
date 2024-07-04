import requests

def number_of_subscribers(subreddit):
    # Set the URL for the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set the headers with a custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'CustomUserAgent/0.1'}
    
    try:
        # Make the GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Return the number of subscribers
            return data['data']['subscribers']
        else:
            # If the subreddit is invalid or another error occurs, return 0
            return 0
    except Exception as e:
        # If an exception occurs, print it and return 0
        print(f"An error occurred: {e}")
        return 0

# Example usage:
subreddit_name = 'python'
print(f"The number of subscribers in r/{subreddit_name} is {number_of_subscribers(subreddit_name)}")

