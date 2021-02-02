#######
# IMPORT PACKAGES
#######

import praw
import pandas as pd

def get_date(created):
    return dt.datetime.fromtimestamp(created)

# Acessing the reddit api


reddit = praw.Reddit(client_id="r30qVuCiSeknQw",#my client id
                     client_secret="T-gV-zXnipmTbvpTlZICVHs7v8PG6Q",  #your client secret
                     user_agent="my user agent", #user agent name
                     username = "Total_Soup_7131",     # your reddit username
                     password = "1pepper2")     # your reddit password

subreddit = reddit.subreddit('Wallstreetbetsnew')  # make a list of subreddits you want to scrape the data from


top_subreddit = subreddit.top()



topics_dict = { "title":[], 
                "score":[], 
                "id":[],
                "url":[], 
                "comms_num": [],
                "created": [], 
                "body":[]
                }

    for submission in subreddit.top(limit=1):
        topics_dict["title"].append(submission.title)
        topics_dict["score"].append(submission.score)
        topics_dict["id"].append(submission.id)
        topics_dict["url"].append(submission.url)
        topics_dict["comms_num"].append(submission.num_comments)
        topics_dict["created"].append(submission.created)
        topics_dict["body"].append(submission.selftext)



        post_dict = {
            "title" : [],
            "score" : [],
            "id" : [],
            "url" : [],
            "comms_num": [],
            "created" : [],
            "body" : []
        }
        comments_dict = {
            "comment_id" : [],
            "comment_parent_id" : [],
            "comment_body" : [],
            "comment_link_id" : [],
            "created" : []
        }
        for submission in subreddit.search(query,sort = "top",limit = 3):
            topics_dict["title"].append(submission.title)
            topics_dict["score"].append(submission.score)
            topics_dict["id"].append(submission.id)
            topics_dict["url"].append(submission.url)
            topics_dict["comms_num"].append(submission.num_comments)
            topics_dict["created"].append(submission.created)
            topics_dict["body"].append(submission.selftext)
            
            ##### Acessing comments on the post
            submission.comments.replace_more(limit = 100)
            for comment in submission.comments.list():
                comments_dict["comment_id"].append(comment.id)
                comments_dict["comment_parent_id"].append(comment.parent_id)
                comments_dict["comment_body"].append(comment.body)
                comments_dict["comment_link_id"].append(comment.link_id)
                comments_dict["created"].append(comment.created)


timestamp = topics_data["created"].apply(get_date)
topics_data = topics_data.assign(timestamp = _timestamp)


        post_comments = pd.DataFrame(comments_dict)

        post_comments.to_csv(s+"_comments_"+ item +"subreddit.csv")
        post_data = pd.DataFrame(post_dict)
        post_data.to_csv(s+"_"+ item +"subreddit.csv")



topics_data = pd.DataFrame(topics_dict)
topics_data.to_csv("reddit_data.csv")
print(topics_data.head())
