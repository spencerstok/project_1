#######
# IMPORT PACKAGES
#######

import praw
import pandas as pd
import time
import datetime as dt

def get_date(created):
    return dt.datetime.fromtimestamp(created)

# Acessing the reddit api
import httplib2
from bs4 import BeautifulSoup, SoupStrainer

urls = []
#gme
#amc
#bb
scrape_urls = ['https://www.reddit.com/search/?q=%24gme&source=recent',
               'https://www.reddit.com/search/?q=%24amc&source=recent',
               'https://www.reddit.com/search/?q=%24bb&source=recent',
               'https://www.reddit.com/search/?q=%24kodk&source=recent']
               
for url in scrape_urls:
    http = httplib2.Http()
    status, response = http.request(url)

    for link in BeautifulSoup(response, 'html.parser',
                              parse_only=SoupStrainer('a')):
        if link.has_attr('href'):
            if "comments" in str(link['href']):
                urls.append(link['href'])
                print(link['href'])


print(urls)
print('-----------------------------------')

url_list = list(set(urls))
print(url_list)
reddit = praw.Reddit(client_id="r30qVuCiSeknQw",#my client id
                     client_secret="T-gV-zXnipmTbvpTlZICVHs7v8PG6Q",  #your client secret
                     user_agent="my user agent", #user agent name
                     username = "Total_Soup_7131",     # your reddit username
                     password = "1pepper2")     # your reddit password


comments_dict = {
    "comment_id": [],
    "created" : [],
    "body" : []
    }

##urls = ['https://www.reddit.com/r/Wallstreetbetsnew/comments/l6i12n/gme_to_the_fuking_moon_upvote_if_holding_till_1k/',
##        'https://www.reddit.com/r/WallStreetbetsELITE/comments/l68les/upvote_dont_lose_faith_plenty_of_orders_on_amc/',
##        'https://www.reddit.com/r/wallstreetbets/comments/l7s631/gme_breakfast_club_megathread/'
##        'https://www.reddit.com/r/wallstreetbets/comments/l6er79/the_gme_afterhours_thread_part_420_on_27_january/'
##        'https://www.reddit.com/r/wallstreetbets/comments/l7v9o8/gme_what_about_second_breakfast_club_megathread/',
##        'https://www.reddit.com/r/wallstreetbets/comments/l65p3u/the_gme_thread_part_2_for_january_27_2021/',
##        'https://www.reddit.com/r/wallstreetbets/comments/l5ne0q/the_gme_thread_part_3_for_january_26_2020/',
##        'https://www.reddit.com/r/wallstreetbets/comments/l78uct/gme_yolo_update_jan_28_2021/',
##        'https://www.reddit.com/r/wallstreetbets/comments/l846a1/gme_yolo_monthend_update_jan_2021/',
##        'https://www.reddit.com/r/wallstreetbets/comments/l6cb1x/the_gme_thread_part_314_for_january_27_2021/',
##        'https://www.reddit.com/r/wallstreetbets/comments/l5xpai/the_gme_thread_for_january_27_2020/',
##        'https://www.reddit.com/r/wallstreetbets/comments/l5c0nr/the_gme_thread_part_1_for_january_26_2021/',
##        'https://www.reddit.com/r/wallstreetbets/comments/l4lmrx/gme_thoughts_yolos_gains_stonk_updates_they_all/',
##        'https://www.reddit.com/r/wallstreetbets/comments/l81n15/gme_afternoon_pajama_party_megathread/',
##        'https://www.reddit.com/r/wallstreetbets/comments/l6vhy3/gme_containment_zone_1_for_28_january/',
##        'https://www.reddit.com/r/wallstreetbets/comments/l6y25u/americans_cant_buy_gme_bb_help_is_on_the_way/',
##        'https://www.reddit.com/r/wallstreetbets/comments/l692dj/the_gme_thread_part_21_for_january_27_2021/',
##        'https://www.reddit.com/r/wallstreetbets/comments/l6ekdz/gme_yolo_update_jan_27_2021_guess_i_need_102/',
##        'https://www.reddit.com/r/wallstreetbets/comments/l6ekdz/gme_yolo_update_jan_27_2021_guess_i_need_102/',        
##        
##
##
##        ]

for url in url_list:

    try:
        submission = reddit.submission(url=url)
    except:
        submission = reddit.submission(url="https://www.reddit.com"+url)
        

    submission.comments.replace_more(limit=0)

    for top_level_comment in submission.comments:

##        print(top_level_comment.body)
        comments_dict["comment_id"].append(top_level_comment.id)
        comments_dict["created"].append(top_level_comment.created)
        comments_dict["body"].append(top_level_comment.body)
        
##        print(top_level_comment.created)
    ##    time.sleep(2)



comments_data = pd.DataFrame(comments_dict)

timestamp = comments_data["created"].apply(get_date)
comments_data = comments_data.assign(timestamp = timestamp)


comments_data.to_csv("reddit_data_full.csv")
