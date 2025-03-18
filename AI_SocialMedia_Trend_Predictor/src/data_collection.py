import os
import tweepy
import pandas as pd
from dotenv import load_dotenv

# Load your environment variables from .env
load_dotenv()

# Twitter API Bearer Token from your .env
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

# Authenticate to Twitter API using Bearer Token
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Function to collect tweets
def collect_tweets(hashtag, count=100):
    print(f"Collecting Tweets for hashtag: {hashtag}")
    
    tweets_data = []
    
    # Use the client to fetch tweets with the hashtag
    # Note: Twitter API v2 search has a different query structure
    response = client.search_recent_tweets(
        query=hashtag,  # Query to search for
        max_results=count,  # Number of tweets to retrieve
        tweet_fields=["created_at", "public_metrics"],  # Specify the fields you want
        user_fields=["username"]
    )

    for tweet in response.data:
        tweet_text = tweet.text
        tweet_id = tweet.id
        created_at = tweet.created_at
        username = tweet.author_id  # You can later fetch user info if needed

        # Collect tweet data
        tweets_data.append({
            "username": username,
            "text": tweet_text,
            "created_at": created_at
        })

    # Convert to pandas DataFrame
    df = pd.DataFrame(tweets_data)
    
    # Save raw data to CSV in data/raw/
    raw_data_path = os.path.join("data", "raw", f"{hashtag.strip('#')}_tweets.csv")
    df.to_csv(raw_data_path, index=False)
    
    print(f"Collected {len(df)} tweets and saved to {raw_data_path}")
    
    return df
