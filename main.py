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

while True:
    for submission in reddit.subreddit("Jokes").new(limit=10):
        if len(submission.selftext)<=280 and len(submission.title)<=120:
            joke_list.append(submission.title + "\n"+ submission.selftext)

    for jokes in range(0,1):
        sleep(1800)
        tweet=joke_list[jokes]
        try:
            api.update_status(tweet)
            print("Tweet is Sent")
        except:
            print("Error")
