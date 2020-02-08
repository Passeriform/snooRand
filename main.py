"""Main handler for flask application.

The handler holds and fetches all configs and configures the flask app.
"""
import os
import random
import json
import re
import markdown2
import praw
import dotenv

from flask import Flask, render_template

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

dotenv.load_dotenv(dotenv_path=os.path.join(BASE_DIR, '.env'))

SUBS = json.load(open(os.path.join(BASE_DIR, 'config', 'subs.json')))

LIMIT = 100

app = Flask(__name__)


@app.route('/')
def home():
    """Define default landing route."""
    return render_template('index.html', subs=SUBS)


@app.route('/<sub_name>')
def display_post(sub_name):
    """Define posts view route."""
    reddit = praw.Reddit(
        client_id=os.getenv('CREDENTIALS_CLIENT_ID'),
        client_secret=os.getenv('CREDENTIALS_CLIENT_SECRET'),
        username=os.getenv('CREDENTIALS_USERNAME'),
        password=os.getenv('CREDENTIALS_PASSWORD'),
        user_agent=os.getenv('CREDENTIALS_USER_AGENT'))

    try:
        sub = reddit.subreddit(sub_name)
        sub_hot = sub.hot(limit=LIMIT)
        random_post = random.choice(list(sub_hot))
    except Exception as snoo_strace:
        return render_template('error.html', stacktrace=snoo_strace)

    image_url = random_post.url
    body = markdown2.markdown(random_post.selftext)

    if '.png' not in image_url and '.jpg' not in image_url and '.jpeg' not in image_url:
        image_url = None

    return render_template("display_post.html",
                           sub=random_post.subreddit.display_name,
                           url=random_post.url,
                           title=random_post.title,
                           author=random_post.author.name,
                           body=body,
                           image=image_url,
                           upvote_ratio=int(random_post.upvote_ratio * 100))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
