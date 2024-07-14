#!/usr/bin/python3

import requests
from collections import Counter

def count_words(subreddit, word_list):
    """
    Recursively queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords (case-insensitive, delimited
    by spaces).
    
    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): A list of keywords to count.
    """
    # Base case: if the subreddit is invalid, return
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    if response.status_code != 200:
        return

    # Parse the titles of the hot articles
    titles = [post["data"]["title"].lower() for post in response.json()["data"]["children"]]

    # Count the occurrences of each keyword in the titles
    all_words = " ".join(titles).split()
    word_counts = Counter([word for word in all_words if word in [w.lower() for w in word_list] and word not in ["java."", "java!", "java_"]])

    # Print the results in descending order by count, then alphabetically
    for word, count in sorted(word_counts.items(), key=lambda x: (-x[1], x[0])):
        print(f"{word}: {count}")

    # Recursively call the function with the "next" page of hot articles
    after = response.json()["data"]["after"]
    if after:
        count_words(subreddit, word_list)




