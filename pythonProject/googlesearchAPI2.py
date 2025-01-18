# Google Search API Using RapidAPI
# This script performs a Google search for "Elon Musk" using the RapidAPI Google Search API
# and retrieves the title and link of the top search result.

import requests  # For making API requests

# API endpoint and parameters for the search query
url = "https://google-search3.p.rapidapi.com/api/v1/search/q=elon+musk&num=100"

# Headers containing API key and other necessary parameters
headers = {
    'x-user-agent': "desktop",  # Specify the user-agent for the search query
    'x-proxy-location': "US",  # Specify the location for the search query
    'x-rapidapi-host': "google-search3.p.rapidapi.com",  # Host header for the API
    'x-rapidapi-key': "cb12f5da9emsh4a615c4a900a1a8p12379cjsnc893378f0af6"  # Replace with your valid API key
}

# Make the GET request to the API
response = requests.request("GET", url, headers=headers)

# Print the raw response text (for debugging purposes)
print(response.text)

# Parse the response JSON
try:
    data = response.json()  # Convert the JSON response to a Python dictionary
    print(type(data))  # Print the type of the response object (should be a dictionary)

    # Extract and display the title and link of the top search result
    top_result_title = data["results"][0]['title']
    top_result_link = data["results"][0]['link']
    print(f"Title: {top_result_title}")
    print(f"Link: {top_result_link}")
except KeyError:
    print("Unexpected response structure or missing keys in the JSON response.")
except ValueError:
    print("Response is not in valid JSON format.")
except Exception as e:
    print(f"An error occurred: {e}")
