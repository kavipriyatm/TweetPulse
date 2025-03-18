# src/api.py
from flask import Flask, jsonify
from collections import Counter
import pandas as pd
from src.trend_predictor import analyze_keywords

app = Flask(__name__)

@app.route('/api/hashtags', methods=['GET'])
def get_trending_hashtags():
    tweets_df = pd.read_csv('data/processed/AI_cleaned_tweets.csv')
    hashtag_counts = analyze_keywords(tweets_df)
    top_hashtags = hashtag_counts.most_common(10)
    
    # Return the top hashtags as JSON
    return jsonify(dict(top_hashtags))

if __name__ == '__main__':
    app.run(debug=True)
