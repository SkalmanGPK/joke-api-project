import requests as r
import string
import time
import os
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
    temp = ""
    for ch in text:
        for i in string.printable:
            if i == ch or ch == "":
                time.sleep(0.01)
                print(temp + i, end='\r', flush=True)
                temp += ch
                break
            else:
                time.sleep(0.01)
                print(temp + i, end='\r', flush=True)
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
def main():
    joke = fetch_joke()
    display_joke(joke)
if __name__ == "__main__":
    main()