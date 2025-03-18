from src.sentiment import process_tweets
from src.trend_predictor import run_trend_analysis

if __name__ == "__main__":
    # Process the tweets, clean them, and perform sentiment analysis
    process_tweets()
    
    # After processing, run trend analysis and prediction
    predicted_trend = run_trend_analysis()
    print(f"The predicted trend based on sentiment is: {predicted_trend}")
