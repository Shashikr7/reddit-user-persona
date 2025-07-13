import praw
import os
from dotenv import load_dotenv
from urllib.parse import urlparse

load_dotenv()

def get_reddit_instance():
    return praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT")
    )

def extract_username(url_or_username):
    if url_or_username.startswith("http"):
        return url_or_username.rstrip("/").split("/")[-1]
    return url_or_username

def fetch_user_data(url_or_username, limit=100):
    reddit = get_reddit_instance()
    username = extract_username(url_or_username)
    user = reddit.redditor(username)

    posts = []
    comments = []

    for submission in user.submissions.new(limit=limit):
        posts.append((submission.title, submission.selftext))

    for comment in user.comments.new(limit=limit):
        comments.append(comment.body)

    return posts, comments
