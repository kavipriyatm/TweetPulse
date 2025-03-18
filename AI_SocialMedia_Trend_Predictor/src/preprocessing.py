import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def preprocess_data(tweets_df):
    # Tokenization
    tweets_df['tokens'] = tweets_df['text'].apply(word_tokenize)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tweets_df['cleaned_text'] = tweets_df['tokens'].apply(lambda tokens: [word for word in tokens if word.lower() not in stop_words])
    
    return tweets_df
