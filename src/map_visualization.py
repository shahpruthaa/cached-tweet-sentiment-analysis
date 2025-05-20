import folium

def create_sentiment_map(tweets):
    tweet_map = folium.Map(location=[20, 0], zoom_start=2)
    
    sentiment_colors = {"Positive": "green", "Negative": "red", "Neutral": "blue"}
    
    for tweet in tweets:
        if tweet["geo"]:
            lat, lon = tweet["geo"]["coordinates"]
            sentiment = tweet["sentiment"]
            folium.CircleMarker(
                location=[lat, lon],
                radius=6,
                color=sentiment_colors[sentiment],
                fill=True,
                fill_opacity=0.6,
                popup=tweet["text"]
            ).add_to(tweet_map)
    
    tweet_map.save("sentiment_map.html")
