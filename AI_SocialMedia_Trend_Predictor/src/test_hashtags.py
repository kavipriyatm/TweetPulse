# test/test_hashtags.py
import unittest
import pandas as pd
from src.trend_predictor import analyze_keywords

class TestHashtagAnalysis(unittest.TestCase):
    
    def setUp(self):
        # Sample input data for testing
        self.tweet_data = pd.DataFrame({
            'cleaned_text': ['#AI is awesome', 'Learning #AI and #ML', '#DataScience rules']
        })
    
    def test_analyze_keywords(self):
        hashtag_counts = analyze_keywords(self.tweet_data)
        self.assertEqual(hashtag_counts['#AI'], 2)
        self.assertEqual(hashtag_counts['#ML'], 1)
        self.assertEqual(hashtag_counts['#DataScience'], 1)

if __name__ == '__main__':
    unittest.main()
