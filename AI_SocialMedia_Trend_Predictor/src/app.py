from flask import Flask, jsonify
import pandas as pd
import os

app = Flask(__name__)

# Endpoint to get sentiment data
@app.route('/sentiment-data', methods=['GET'])
def get_sentiment_data():
    df = pd.read_csv('data/processed/AI_cleaned_tweets.csv')  # Your sentiment analysis data
    sentiment_counts = df['sentiment'].value_counts().to_dict()  # Get sentiment counts (positive, neutral, negative)
    return jsonify(sentiment_counts)  # Send it as JSON

# Endpoint to get the word cloud image URL
@app.route('/word-cloud', methods=['GET'])
def get_word_cloud():
    # You already saved the word cloud image as 'word_cloud.png' in 'outputs/figures'
    return jsonify({"image_url": "/outputs/figures/word_cloud.png"})  # Send the URL of the word cloud image

if __name__ == '__main__':
    app.run(debug=True)
