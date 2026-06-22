import nltk
from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer
from transformers import pipeline

nltk.download('vader_lexicon', quiet=True)
sia = SentimentIntensityAnalyzer()
sentiment_pipeline = pipeline(
    model="lxyuan/distilbert-base-multilingual-cased-sentiments-student",
    device=-1
)


def analyze_sentiment(user_input: str) -> float:
    textblob_polarity = TextBlob(user_input).sentiment.polarity
    vader_polarity = sia.polarity_scores(user_input)['compound']
    transformer_result = sentiment_pipeline(user_input)[0]
    transformer_score = transformer_result['score']

    if transformer_result['label'] == 'negative':
        transformer_score = -transformer_score

    return (textblob_polarity + vader_polarity + transformer_score) / 3
