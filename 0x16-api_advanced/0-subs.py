#!/usr/bin/python3

def top_ten(subreddit):
    try:
        # Construct the API URL for the given subreddit
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

        # Set the headers to include the 'User-Agent' header
        headers = {'User-Agent': 'my-app/0.0.1'}

        # Make the GET request to the API
        response = requests.get(url, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            # Get the JSON data from the response
            data = response.json()

            # Extract the titles of the first 10 hot posts
            titles = [post['data']['title'] for post in data['data']['children']]

            # Print the titles
            for title in titles:
                print(title)
        else:
            # If the request was not successful, print None
            print(None)
    except:
        # If there is an error, print None
        print(None)

