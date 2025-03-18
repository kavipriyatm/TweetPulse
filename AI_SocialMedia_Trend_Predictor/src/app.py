from flask import Flask, jsonify
import pandas as pd
import os

app = Flask(__name__)

@app.route('/sentiment-data', methods=['GET'])
def get_sentiment_data():
    df = pd.read_csv('data/processed/AI_cleaned_tweets.csv')  
    sentiment_counts = df['sentiment'].value_counts().to_dict()  
    return jsonify(sentiment_counts) 


@app.route('/word-cloud', methods=['GET'])
def get_word_cloud():

    return jsonify({"image_url": "/outputs/figures/word_cloud.png"}) 
if __name__ == '__main__':
    app.run(debug=True)
