from src.load_data import load_cached_tweets
from src.sentiment_analysis import analyze_sentiment
from src.map_visualization import create_sentiment_map

def run():
    tweets = load_cached_tweets()
    
    for tweet in tweets:
        tweet["sentiment"] = analyze_sentiment(tweet["text"])
    
    create_sentiment_map(tweets)
    print("Sentiment map saved to 'sentiment_map.html'")

if __name__ == "__main__":
    run()
