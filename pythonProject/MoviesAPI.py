# IMDB - Internet Movie Database (Unofficial) API Example
# This script fetches movie details such as title and rating from the IMDB unofficial API using RapidAPI.

import requests  # Import requests module for making HTTP requests

# Define the API endpoint for fetching movie details
url = "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/Avergers"  # Replace 'Avergers' with the correct movie name or query

# Set up the API headers, including host and API key for authentication
headers = {
    'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com",
    'x-rapidapi-key': "cb12f5da9emsh4a615c4a900a1a8p12379cjsnc893378f0af6"  # Replace with your valid API key
}

# Make a GET request to the API
response = requests.request("GET", url, headers=headers)

# Print the raw JSON response text for debugging
print(response.text)

# Parse the JSON response into a Python dictionary
data = response.json()

# Check the type of the parsed data (it should be a dictionary)
print(type(data))

# Extract and print specific details from the API response
print("Title:", data["title"])  # Print the movie title
print("Rating:", data["rating"])  # Print the movie rating
