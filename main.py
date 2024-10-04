import requests as r
import string
import time
import os
import tweepy
def fetch_joke():
    url = "https://v2.jokeapi.dev/joke/Any"
    response = r.get(url)

    if response.status_code == 200: # Checks if the fetch worked
        joke_data = response.json()
        if joke_data["type"] == "single": # One line joke
            return joke_data["joke"]
        else: # Joke with setup and delivery
            return f"{joke_data['setup']} ... {joke_data['delivery']}"
    else:
        return " Failed to fetch joke"
def display_joke(text): # fun way to display text, like raindrops
    clear()
    print(text)
    #temp = ""
    #for ch in text:
        #for i in string.printable:
            #if i == ch or ch == "":
                #time.sleep(0.01)
                #print(temp + i, end='\r', flush=True)
                #temp += ch
                #break
            #else:
                #time.sleep(0.01)
                #print(temp + i, end='\r', flush=True)
# Function to authenticate and post on twitter
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
    #function to tweet the joke
def tweet_joke(joke_text):
    client = authenticate_twitter()
    try:
        #Post the joke as a tweet
        client.create_tweet(text=joke_text)
        print("joke shared on twitter!")
    except tweepy.TweepyException as e:
        print(f"Failed to post tweet : {e}")
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
def main():
    joke = fetch_joke()
    display_joke(joke)
    while True:
        print("\nWould you like to share this joke on twitter? (yes/no)")
        share = input(" > ")
        if share.lower() == "yes":
            tweet_joke(joke)
            break
        elif share.lower() == "no":
            print("Okay have a good day!")
            break
        else:
            print("error input, try again")
    
if __name__ == "__main__":
    main()