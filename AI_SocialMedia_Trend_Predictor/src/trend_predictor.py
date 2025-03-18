import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import re
import os

# Load the cleaned and processed tweet data
def load_processed_data():
    file_path = 'data/processed/AI_cleaned_tweets.csv'
    
    if not os.path.exists(file_path):
        print(f"Error: The file {file_path} does not exist.")
        return pd.DataFrame()  # Return an empty DataFrame if the file doesn't exist
    
    tweets_df = pd.read_csv(file_path)
    return tweets_df

# Function to extract hashtags from text
def extract_hashtags(text):
    # Find all hashtags in the text using a regular expression
    return re.findall(r'#\w+', text)

# Function to analyze the frequency of hashtags or keywords in tweets
def analyze_keywords(tweets_df):
    # Extract hashtags from each tweet's cleaned text
    hashtags = []
    for text in tweets_df['cleaned_text']:
        hashtags.extend(extract_hashtags(text))  # Add all found hashtags to the list
    
    if not hashtags:
        print("No hashtags found in the tweets.")
        return Counter()  # Return an empty Counter if no hashtags are found
    
    # Count the frequency of each hashtag
    hashtag_counts = Counter(hashtags)
    return hashtag_counts

# Function to plot trending hashtags
def plot_trending_hashtags(hashtag_counts):
    if not hashtag_counts:  # Check if no hashtags were found
        print("No hashtags to plot.")
        return
    
    # Get the top 10 trending hashtags
    top_hashtags = hashtag_counts.most_common(10)
    if not top_hashtags:  # Check if top hashtags is empty
        print("No trending hashtags to display.")
        return
    
    hashtags, counts = zip(*top_hashtags)
    
    # Plotting the trending hashtags
    plt.figure(figsize=(10, 5))
    plt.bar(hashtags, counts, color='skyblue')
    plt.title('Top 10 Trending Hashtags')
    plt.xlabel('Hashtags')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Save and show the plot
    output_path = 'outputs/figures/trending_hashtags.png'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)  # Create output folder if it doesn't exist
    plt.savefig(output_path)
    plt.show()

# Function to predict trends based on tweets
def predict_trends():
    # Load processed data
    tweets_df = load_processed_data()
    
    if tweets_df.empty:  # Check if the DataFrame is empty
        print("No data available for trend prediction.")
        return
    
    # Analyze the keywords (hashtags in this case)
    hashtag_counts = analyze_keywords(tweets_df)
    
    # Plot the trending hashtags
    plot_trending_hashtags(hashtag_counts)

# Main function to run the entire process
if __name__ == "__main__":
    predict_trends()
