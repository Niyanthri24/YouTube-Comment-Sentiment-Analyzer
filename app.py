import streamlit as st # type: ignore
import pandas as pd
from youtube_scraper import get_comments
from sentiment import analyze_sentiment

st.set_page_config(page_title="YouTube Sentiment Analyzer", layout="wide")
st.title("🎥 YouTube Comment Sentiment Analyzer")

video_url = st.text_input("Paste a YouTube video URL:", "")

max_comments = st.slider("Number of comments to analyze", min_value=5, max_value=50, value=20)

if st.button("Analyze"):
    with st.spinner("Fetching and analyzing comments..."):
        comments = get_comments(video_url, max_comments=max_comments)
        sentiments = analyze_sentiment(comments)

        df = pd.DataFrame({
            "Comment": comments,
            "Sentiment": [res['label'] for res in sentiments],
            "Confidence": [round(res['score'], 2) for res in sentiments]
        })

        st.success("Done!")
        st.dataframe(df)

        st.subheader("📊 Sentiment Distribution")
        st.bar_chart(df["Sentiment"].value_counts())
