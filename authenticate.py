import tweepy
def authenticate_twitter():
    API_key = "kj12ekAIyEevX9jzUh97jnoZk"
    API_key_secret = "gm7BLvQTIYfLioCqz7ECELsk4IzVRsF3SzmbmAluuEnrrpL2xV"
    bearer_token = "AAAAAAAAAAAAAAAAAAAAAGnTwAEAAAAAAN4T1Klb9nYoz3Urox2hB9d0HD4%3DtzRzTIwcVEHxveUqO5iq8IWgFj9BgyeOs7en1rIy8tx7wcQDHL"
    access_token = "1841787307424133120-x5PqcqQ5mZYqkecaLpoDLhYIP3vPjc"
    access_token_secret = "TRWkZXVsAcLqpyT9DcnfPDti5t2GBFYWOgfXo2UzBPg7O"

    # Authenticate with Twitter API
    client = tweepy.Client(bearer_token, API_key, API_key_secret, access_token, access_token_secret)
    auth = tweepy.OAuth1UserHandler(API_key, API_key_secret, access_token, access_token_secret)
    api = tweepy.API(auth)
    return client