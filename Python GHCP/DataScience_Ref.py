import pandas as pd
import nltk
nltk.download('vader_lexicon')

from nltk.sentiment import SentimentIntensityAnalyzer

# Read the CSV file
df = pd.read_csv('sentiment.csv')

# Initialize the VADER sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Perform sentiment analysis on each feedback
df['sentiment'] = df['feedback'].apply(lambda x: sia.polarity_scores(x)['compound'])

# Categorize the sentiment
df['sentiment_category'] = df['sentiment'].apply(lambda x: 'positive' if x > 0 else 'negative' if x < 0 else 'neutral')

# Display the feedback along with its sentiment category
print(df[['feedback', 'sentiment_category']])