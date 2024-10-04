import requests as r
#import string
#import time
import json
import os
import tweepy
import authenticate as a
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
        return "Failed to fetch joke"
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
def tweet_joke(joke_text):
    if is_duplicate(joke_text):
        print("This joke has already been tweeted!")
    else:
        client = a.authenticate_twitter()
        try:
            #Post the joke as a tweet
            client.create_tweet(text=joke_text)
            print("joke shared on twitter!")
            log_tweet(joke_text)
        except tweepy.TweepyException as e:
            print(f"Failed to post tweet : {e}")
def log_tweet(joke_text):
    #Load existing tweets from JSON
    tweets = load_tweets()
    print(f"Logging tweet: {joke_text}")
    # Add the new tweet to the list
    tweets.append(joke_text)
    # Write the updated list back to the JSON file
    try:
        with open("tweet_log.json", 'w') as file:
            json.dump(tweets, file, indent=4)
        print("Tweet logged successfully")
    except Exception as e:
        print(f"Error logging tweet: {e}")

# Function to check if the joke has already been logged
def is_duplicate(joke_text):
    tweets = load_tweets()
    return joke_text in tweets

# Function to load tweets from the JSON file
def load_tweets():
    if not os.path.exists("tweet_log.json"):
        print("No tweet log found, creating new log.")
        return [] # If no file exists, return an empty list
    # Load the JSON file
    try:
        with open("tweet_log.json", 'r') as file:
            data = file.read().strip()  # Read the file and remove any surrounding spaces or newlines
            if not data: # Check if the file is empty
                print("Tweet log is empty")
                return [] # Return an empty list if the file is empty
            return json.loads(data) # Parse and return the JSON data
    except (json.JSONDecodeError, ValueError):
        # Handle invalid JSON format
        print("Error reading tweet log, returning empty list")
        return [] # If the file is corrupted or invalid, return an empty list

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