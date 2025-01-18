"""
This script fetches a random quote using the RapidAPI Quotes API.
It prints the quote's unique ID and its content.
"""

import requests  # Library for making HTTP requests

# Define the API endpoint
url = "https://quotes15.p.rapidapi.com/quotes/random/"

# Define the headers with RapidAPI credentials
headers = {
    'x-rapidapi-host': "quotes15.p.rapidapi.com",  # Host for the Quotes API
    'x-rapidapi-key': "cb12f5da9emsh4a615c4a900a1a8p12379cjsnc893378f0af6"  # Replace with your API key
}

# Send a GET request to fetch a random quote
response = requests.request("GET", url, headers=headers)

# Parse the JSON response
try:
    CovData = response.json()  # Convert the response to JSON format
    print("Quote ID:", CovData["id"])  # Print the unique ID of the quote
    print("Quote Content:", CovData["content"])  # Print the quote's text
except KeyError as e:
    print("Error: Unable to fetch data. Key missing:", e)
except Exception as e:
    print("Error: An unexpected error occurred:", e)

# Uncomment the following lines for debugging
# print(response.text)  # Raw response text
# print(type(response.json()))  # Type of the parsed response
