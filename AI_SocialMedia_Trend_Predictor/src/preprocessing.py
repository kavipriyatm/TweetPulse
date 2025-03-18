import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def preprocess_data(tweets_df):

    tweets_df['tokens'] = tweets_df['text'].apply(word_tokenize)
    
 
    stop_words = set(stopwords.words('english'))
    tweets_df['cleaned_text'] = tweets_df['tokens'].apply(lambda tokens: [word for word in tokens if word.lower() not in stop_words])
    
    return tweets_df
