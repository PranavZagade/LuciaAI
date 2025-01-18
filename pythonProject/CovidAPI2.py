# COVID-19 Data Retrieval for Asia Using Free RapidAPI
# This script fetches COVID-19 data for Asian countries using the Vaccovid API.
# It demonstrates how to make API requests, handle responses, and extract specific data.

import requests  # Library for making HTTP requests

# API endpoint for retrieving COVID-19 data for Asia
url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/npm-covid-data/asia"

# Headers for authentication and host specification
headers = {
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com",
    'x-rapidapi-key': "cb12f5da9emsh4a615c4a900a1a8p12379cjsnc893378f0af6"  # Replace with your valid API key
}

# Making a GET request to the API
response = requests.request("GET", url, headers=headers)

# Print the raw response text (useful for debugging)
print(response.text)

# Convert the response to a JSON object
data = response.json()

# Print the first record for inspection
print(data[0])

# Extract and print the 'Country' field from the first record
print(f"Country: {data[0]['Country']}")

# Optional: Loop through the data to print the country names
'''
for record in data:
    print(f"Country: {record['Country']}, Total Cases: {record['TotalCases']}, Deaths: {record['TotalDeaths']}")
'''
