# reddit_service.py

import praw
from collections import Counter

def create_reddit_instance():
    from config import USERNAME, PASSWORD, CLIENT_ID, CLIENT_SECRET, USER_AGENT, CHECK_FOR_ASYNC
    return praw.Reddit(username=USERNAME,
                       password=PASSWORD,
                       client_id=CLIENT_ID,
                       client_secret=CLIENT_SECRET,
                       user_agent=USER_AGENT,
                       check_for_async=CHECK_FOR_ASYNC)

def get_subreddits(reddit, username):
    redditor = reddit.redditor(username)
    subreddit_counter = Counter()

    for submission in redditor.submissions.new(limit=None):
        subreddit_counter[submission.subreddit.display_name] += 1

    return subreddit_counter.most_common()

def search_reddit(reddit, username, search_string):
    redditor = reddit.redditor(username)
    matching_posts = []
    matching_comments = []

    for submission in redditor.submissions.new(limit=None):
        if search_string.lower() in submission.title.lower():
            matching_posts.append(submission.title)

    for comment in redditor.comments.new(limit=None):
        if search_string.lower() in comment.body.lower():
            matching_comments.append(comment.body)

    return matching_posts, matching_comments
