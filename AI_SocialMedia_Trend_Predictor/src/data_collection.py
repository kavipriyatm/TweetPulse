import os
import tweepy
import pandas as pd
from dotenv import load_dotenv


load_dotenv()


BEARER_TOKEN = os.getenv("BEARER_TOKEN")


client = tweepy.Client(bearer_token=BEARER_TOKEN)

def collect_tweets(hashtag, count=100):
    print(f"Collecting Tweets for hashtag: {hashtag}")
    
    tweets_data = []
    
   
    response = client.search_recent_tweets(
        query=hashtag,  
        max_results=count,  
        tweet_fields=["created_at", "public_metrics"],  
        user_fields=["username"]
    )

    for tweet in response.data:
        tweet_text = tweet.text
        tweet_id = tweet.id
        created_at = tweet.created_at
        username = tweet.author_id 

       
        tweets_data.append({
            "username": username,
            "text": tweet_text,
            "created_at": created_at
        })

    df = pd.DataFrame(tweets_data)
    
 
    raw_data_path = os.path.join("data", "raw", f"{hashtag.strip('#')}_tweets.csv")
    df.to_csv(raw_data_path, index=False)
    
    print(f"Collected {len(df)} tweets and saved to {raw_data_path}")
    
    return df
