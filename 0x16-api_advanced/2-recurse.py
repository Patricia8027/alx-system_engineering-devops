#!/usr/bin/python3

import requests

def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively queries the Reddit API to get the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to get the hot articles for.
        hot_list (list, optional): The list of hot article titles, defaults to an empty list.
        after (str, optional): The 'after' parameter for pagination, defaults to None.

    Returns:
        list or None: A list of hot article titles, or None if the subreddit is invalid.
    """
    if hot_list is None:
        hot_list = []

    try:
        # Set a custom User-Agent to avoid rate limiting
        headers = {'User-Agent': 'my-reddit-app/1.0'}

        # Query the Reddit API for the subreddit hot articles
        url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'
        if after:
            url += f'&after={after}'
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the request was successful
        if response.status_code == 200:
            # Extract the post titles from the response JSON
            data = response.json()
            hot_list.extend([post['data']['title'] for post in data['data']['children']])

            # Check if there are more pages of results
            after = data['data']['after']
            if after:
                # Recursively call the function with the 'after' parameter
                return recurse(subreddit, hot_list, after)
            else:
                # Return the list of hot article titles
                return hot_list
        else:
            # Return None if the subreddit is invalid
            return None
    except:
        # Return None if any errors occur
        return None



