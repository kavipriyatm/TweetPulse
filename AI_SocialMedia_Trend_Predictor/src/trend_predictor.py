import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import re
import os

def load_processed_data():
    file_path = 'data/processed/AI_cleaned_tweets.csv'
    
    if not os.path.exists(file_path):
        print(f"Error: The file {file_path} does not exist.")
        return pd.DataFrame()  
    
    tweets_df = pd.read_csv(file_path)
    return tweets_df


def extract_hashtags(text):
   
    return re.findall(r'#\w+', text)


def analyze_keywords(tweets_df):
 
    hashtags = []
    for text in tweets_df['cleaned_text']:
        hashtags.extend(extract_hashtags(text))  
    
    if not hashtags:
        print("No hashtags found in the tweets.")
        return Counter()  
    
  
    hashtag_counts = Counter(hashtags)
    return hashtag_counts

def plot_trending_hashtags(hashtag_counts):
    if not hashtag_counts: 
        print("No hashtags to plot.")
        return
    
  
    top_hashtags = hashtag_counts.most_common(10)
    if not top_hashtags: 
        print("No trending hashtags to display.")
        return
    
    hashtags, counts = zip(*top_hashtags)
    

    plt.figure(figsize=(10, 5))
    plt.bar(hashtags, counts, color='skyblue')
    plt.title('Top 10 Trending Hashtags')
    plt.xlabel('Hashtags')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    output_path = 'outputs/figures/trending_hashtags.png'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)
    plt.show()

def predict_trends():
 
    tweets_df = load_processed_data()
    
    if tweets_df.empty:  
        print("No data available for trend prediction.")
        return
    
   
    hashtag_counts = analyze_keywords(tweets_df)
  
    plot_trending_hashtags(hashtag_counts)

# Main function to run the entire process
if __name__ == "__main__":
    predict_trends()
