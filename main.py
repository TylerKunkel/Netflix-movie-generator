import requests
import random
import time

# Make a request to the uNoGS API to retrieve the current list of movies on Netflix
response = requests.get("https://unogsng.p.rapidapi.com/search", headers={
    "X-RapidAPI-Host": "unogsng.p.rapidapi.com",
    "X-RapidAPI-Key": "8645b8f8a0msh8899cd4dd414287p169687jsn6a00d123b3f3",
    "Accept": "application/json"
}, params={
    "countrylist": "78",  # Country code for Netflix US
    "orderby": "rating",  # Order the results by rating
    "limit": "100"  # Limit the results to the first 100 movies
})

# Parse the response to extract the movie titles
movies = [item["title"] for item in response.json()["results"]]

# Define a function to randomly select a movie from the list
def select_movie():
    return random.choice(movies)

# Prompt the user to generate a movie selection
print("Welcome to my Random Netflix Movie Generator!")
print("-------------------------------------------------------------")
print()
time.sleep(1)
print("Press the 'Enter Key' to generate a movie selection!")
print()
print("Type 'quit' to exit")
while True:
    user_input = input()
    if user_input == "":
        movie = select_movie()
        print("I think you should watch:")
        print(movie)
    elif user_input == "quit":
        break
    else:
        print("Invalid input. Press enter to generate a movie selection, or type 'quit' to exit.")
