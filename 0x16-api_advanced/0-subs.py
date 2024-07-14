#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to get the number of subscribers for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to get the subscriber count for.
    
    Returns:
        int: The number of subscribers for the given subreddit, or 0 if the subreddit is invalid.
    """
    try:
        # Set a custom User-Agent to avoid rate limiting
        headers = {'User-Agent': 'my-reddit-app/1.0'}
        
        # Query the Reddit API for the subreddit information
        response = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json', headers=headers, allow_redirects=False)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Extract the number of subscribers from the response JSON
            data = response.json()
            return data['data']['subscribers']
        else:
            # Return 0 if the subreddit is invalid
            return 0
    except:
        # Return 0 if any errors occur
        return 0
