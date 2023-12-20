import praw
import os
from dotenv import load_dotenv
load_dotenv()

app_id = os.getenv("REDDIT_APP_ID")
secret = os.getenv("REDDIT_SECRET")
name = os.getenv("REDDIT_APP_NAME")


reddit = praw.Reddit(
    client_id=app_id,
    client_secret=secret,
    user_agent=name)

submissions = []

def get_submissions(subreddit):
    for submission in reddit.subreddit(subreddit).hot(limit=3):
        submissions.append(submission.title)
    return submissions
        
