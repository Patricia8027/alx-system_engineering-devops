#!/usr/bin/python3

import requests

def top_ten(subreddit):
    """
    Queries the Reddit API to get the titles of the first 10 hot posts for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to get the hot posts for.
    """
    try:
        # Set a custom User-Agent to avoid rate limiting
        headers = {'User-Agent': 'my-reddit-app/1.0'}
        
        # Query the Reddit API for the subreddit hot posts
        response = requests.get(f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10', headers=headers, allow_redirects=False)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Extract the post titles from the response JSON
            data = response.json()
            for post in data['data']['children']:
                print(post['data']['title'])
        else:
            # Print None if the subreddit is invalid
            print(None)
    except:
        # Print None if any errors occur
        print(None)



