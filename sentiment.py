import os
os.environ["TRANSFORMERS_NO_TF"] = "1"

from transformers import pipeline

# Load the sentiment pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(comments):
    return sentiment_pipeline(comments)
