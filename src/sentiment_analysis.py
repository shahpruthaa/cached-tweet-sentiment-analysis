from textblob import TextBlob

def analyze_sentiment(tweet_text):
    analysis = TextBlob(tweet_text)
    polarity = analysis.sentiment.polarity
    if polarity > 0.1:
        return "Positive"
    elif polarity < -0.1:
        return "Negative"
    else:
        return "Neutral"
