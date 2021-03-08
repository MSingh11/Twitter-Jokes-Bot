import tweepy
import praw
import random


auth=tweepy.OAuthHandler("")
auth.set_access_token("")

api=tweepy.API(auth)

reddit=praw.Reddit(
client_id="",
client_secret="",
user_agent="Test")

joke_list=[]

for submission in reddit.subreddit("Jokes").top("day",limit=30):
    if len(submission.selftext)<=280 and len(submission.title)<=120:
        joke_list.append(submission.title + "\n"+ submission.selftext)

for jokes in range(0,5):
    tweet=joke_list[jokes]
    api.update_status(tweet)
    print("Tweet Sent")

