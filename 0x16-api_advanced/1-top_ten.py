#!/usr/bin/python3
def top_ten(subreddit):
    try:
        # Construct the API URL for the given subreddit
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
        
        # Set the headers to include the 'User-Agent' header
        headers = {'User-Agent': 'my-app/0.0.1'}
        
        # Make the GET request to the API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Get the JSON data from the response
            data = response.json()
            
            # Extract the titles of the first 10 hot posts
            titles = [post['data']['title'] for post in data['data']['children']]
            
            # Print the titles
            for title in titles:
                print(title)
        # Check if the request was redirected (status code 30x)
        elif 300 <= response.status_code < 400:
            # If redirected, print None
            print(None)


