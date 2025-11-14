thondef filter_sentiment(posts_or_comments):
    # A simple sentiment filter that excludes negative sentiment posts.
    # In production, this could integrate with sentiment analysis APIs or models.
filtered = [item for item in posts_or_comments if 'negative' not in item.lower()]
return filtered