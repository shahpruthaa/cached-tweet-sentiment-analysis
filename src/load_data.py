import json

def load_cached_tweets(filepath="cached_data/tweets.json"):
    with open(filepath, "r") as f:
        return json.load(f)
