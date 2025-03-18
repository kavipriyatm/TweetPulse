import pandas as pd
import re
import string
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
import os

def load_data():
    tweets_df = pd.read_csv('data/raw/AI_tweets.csv')
    return tweets_df

def clean_text(text):
    text = re.sub(r'http\S+|www\S+', '', text)  
    text = text.translate(str.maketrans('', '', string.punctuation))  
    text = text.lower() 
    stop_words = set(stopwords.words('english'))  s
    text = ' '.join([word for word in text.split() if word not in stop_words])
    return text


def get_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    sentiment_score = sid.polarity_scores(text)['compound']
    if sentiment_score > 0:
        return 'positive'
    elif sentiment_score < 0:
        return 'negative'
    else:
        return 'neutral'


def process_tweets():
    tweets_df = load_data()

   
    tweets_df['cleaned_text'] = tweets_df['text'].apply(clean_text)

   
    tweets_df['sentiment'] = tweets_df['cleaned_text'].apply(get_sentiment)

  
    if not os.path.exists('data/processed'):
        os.makedirs('data/processed')

  
    tweets_df.to_csv('data/processed/AI_cleaned_tweets.csv', index=False)

    return tweets_df

def visualize_data(tweets_df):
  
    sentiment_counts = tweets_df['sentiment'].value_counts()
    sentiment_counts.plot(kind='bar', title='Sentiment Distribution')


    sentiment_counts.plot(kind='bar', title='Sentiment Distribution')
    plt.savefig('outputs/figures/sentiment_distribution.png') 


    all_text = ' '.join(tweets_df['cleaned_text'])
    wordcloud = WordCloud(width=800, height=400).generate(all_text)
    

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.savefig('outputs/figures/word_cloud.png')  
    plt.show()

if __name__ == "__main__":
  
    tweets_df = process_tweets()
    visualize_data(tweets_df)


    tweets_df.to_csv('data/processed_tweets_with_sentiment.csv', index=False)


    print(tweets_df.head())
