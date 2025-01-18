# Web Search and Automated Browser Navigation
# This script performs a Google search using the RapidAPI Google Search API and navigates to the top result using Selenium.

import time  # For sleep delays
import requests  # For making API requests
import webbrowser  # For opening URLs in the default browser
from selenium import webdriver  # For automated browser control

# Define the API endpoint
url = "https://google-search1.p.rapidapi.com/google-search"

# Define the query parameters for the search
querystring = {"hl": "en", "q": "Elon Musk", "gl": "us"}  # hl: language, q: query, gl: country code

# Define the headers with RapidAPI credentials
headers = {
    'x-rapidapi-host': "google-search1.p.rapidapi.com",
    'x-rapidapi-key': "cb12f5da9emsh4a615c4a900a1a8p12379cjsnc893378f0af6"  # Replace with your valid API key
}

# Make the GET request to the API
response = requests.request("GET", url, headers=headers, params=querystring)

# Check the response type and print the raw response
print(type(response.json()))  # Verify the type of the response (should be a dictionary)
data = response.json()  # Parse the JSON response
print(response.text)  # Print the raw response text for debugging

# Extract and display information about the top search result
print(data["organic"][0]["snippet"])  # Print the snippet (summary) of the top result
add = data["organic"][0]["url"]  # Extract the URL of the top result
print(add)  # Print the URL

# Option 1: Open the URL in the default browser (uncomment to use)
# webbrowser.open(add)

# Option 2: Open the URL in an automated Chrome browser
driver = webdriver.Chrome()  # Ensure the ChromeDriver is installed and in PATH
driver.get(add)  # Navigate to the extracted URL
time.sleep(10)  # Keep the browser open for 10 seconds before closing
