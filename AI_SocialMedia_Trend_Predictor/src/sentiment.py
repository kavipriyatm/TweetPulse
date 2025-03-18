import pandas as pd
import re
import string
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
import os

# Load the raw tweet data
def load_data():
    tweets_df = pd.read_csv('data/raw/AI_tweets.csv')
    return tweets_df

# Clean the tweet text
def clean_text(text):
    text = re.sub(r'http\S+|www\S+', '', text)  # Remove links
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    text = text.lower()  # Convert to lowercase
    stop_words = set(stopwords.words('english'))  # Remove stopwords
    text = ' '.join([word for word in text.split() if word not in stop_words])
    return text

# Apply sentiment analysis to the cleaned text
def get_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    sentiment_score = sid.polarity_scores(text)['compound']
    if sentiment_score > 0:
        return 'positive'
    elif sentiment_score < 0:
        return 'negative'
    else:
        return 'neutral'

# Process the tweets
def process_tweets():
    tweets_df = load_data()

    # Clean the tweet texts
    tweets_df['cleaned_text'] = tweets_df['text'].apply(clean_text)

    # Perform sentiment analysis
    tweets_df['sentiment'] = tweets_df['cleaned_text'].apply(get_sentiment)

    # Create the 'processed' folder if it doesn't exist
    if not os.path.exists('data/processed'):
        os.makedirs('data/processed')

    # Save the cleaned data to 'processed' folder
    tweets_df.to_csv('data/processed/AI_cleaned_tweets.csv', index=False)

    return tweets_df

# Visualize sentiment distribution and word cloud
def visualize_data(tweets_df):
    # Sentiment distribution
    sentiment_counts = tweets_df['sentiment'].value_counts()
    sentiment_counts.plot(kind='bar', title='Sentiment Distribution')

    # Save sentiment distribution plot
    sentiment_counts.plot(kind='bar', title='Sentiment Distribution')
    plt.savefig('outputs/figures/sentiment_distribution.png')  # Save as PNG in the 'outputs/figures' directory

    # Word cloud
    all_text = ' '.join(tweets_df['cleaned_text'])
    wordcloud = WordCloud(width=800, height=400).generate(all_text)
    
    # Save word cloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.savefig('outputs/figures/word_cloud.png')  # Save as PNG in the 'outputs/figures' directory
    
    # Show the plots
    plt.show()

# Main function to run the entire process
if __name__ == "__main__":
    # Process the tweets and visualize the data
    tweets_df = process_tweets()
    visualize_data(tweets_df)

    # After processing tweets and sentiment analysis, save the final dataset
    tweets_df.to_csv('data/processed_tweets_with_sentiment.csv', index=False)

    # Optionally, display the first few rows of the processed data
    print(tweets_df.head())
