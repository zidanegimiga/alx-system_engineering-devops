### General Concepts
    How to read API documentation to find the endpoints you are looking for.
    How to use an API with pagination
    How to parse JSON results from an API
    How to make a recursive API call
    How to sort a dictionary by value

### Files
- ###### 0-subs.py
a function that queries the **[Reddit API](https://www.reddit.com/dev/api/) and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function returns 0. <br>
Prototype: `def number_of_subscribers(subreddit)`

- ###### 1-top_ten.py
a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.
Prototype: `def top_ten(subreddit)`

- ###### 2-recurse.py
a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function returns None.
Prototype: `def recurse(subreddit, hot_list=[])`
