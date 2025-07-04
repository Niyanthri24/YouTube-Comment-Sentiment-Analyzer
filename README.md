# YouTube-Comment-Sentiment-Analyzer
A real-time sentiment analysis tool for YouTube comments using BERT and Streamlit.

Just paste a video URL and watch the dashboard populate with live sentiment insights — no API key required!

---

## Tech Stack

- **BERT (Transformers by Hugging Face)** – Pre-trained model for sentiment classification
- **Streamlit** – Lightweight dashboard for real-time visualizations
- **youtube-comment-downloader** – Fetches comments directly without needing the YouTube API
- **Python**, **Pandas**

---

## How to Run the App

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/youtube-sentiment-analyzer.git
   cd youtube-sentiment-analyzer

   pip install -r requirements.txt

   streamlit run app.py

## Project Structure
youtube-sentiment-analyzer/
├── app.py                # Streamlit dashboard
├── sentiment.py          # BERT-based sentiment pipeline
├── youtube_scraper.py    # YouTube comment fetcher
├── requirements.txt      # Required packages
└── README.md             # Documentation

## Sample Link - https://www.youtube.com/watch?v=dQw4w9WgXcQ

## Features
- Real-time comment sentiment classification
- Confidence scores for each sentiment
- Live dashboard with bar charts and tables
- No authentication or API keys required

## Notes: Make sure Keras and TensorFlow are uninstalled if you face errors with Transformers:
  pip uninstall keras tensorflow
