#!/usr/bin/python3
"""
Script to query a list of all hot posts on a given Reddit subreddit.
"""
def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively queries the Reddit API and returns a list of hot article titles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to search.
        hot_list (list, optional): The list of hot article titles. Defaults to an empty list.
        after (str, optional): The 'after' parameter for pagination. Defaults to None.

    Returns:
        list: A list of hot article titles, or None if no results are found.
    """
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    params = {"limit": 100, "after": after}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

    data = response.json()["data"]
    hot_list.extend([post["title"] for post in data["children"]])

    after = data["after"]
    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
