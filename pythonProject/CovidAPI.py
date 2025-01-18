# COVID-19 Data Retrieval Using RapidAPI
# This script fetches COVID-19 data for a specific country using the RapidAPI service.
# It demonstrates how to make API requests, handle responses, and extract specific information.

import requests  # Library for making HTTP requests
from operator import itemgetter  # (Optional) For sorting data based on specific keys

# API endpoint and parameters
url = "https://covid-19-data.p.rapidapi.com/country/code"
countrycode = "in"  # Country code for India

# Query parameters for the API request
querystring = {"code": countrycode}

# Headers for authentication and host specification
headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': "cb12f5da9emsh4a615c4a900a1a8p12379cjsnc893378f0af6"  # Replace with your valid API key
}

# Making a GET request to the API
response = requests.request("GET", url, headers=headers, params=querystring)

# Print the raw response text
print(response.text)

# Convert the response to a JSON object
CovData = response.json()

# Extract and display the country name from the data
print(CovData[0]['country'])

'''
# Example 1: Iterating over keys and values in the response
for key, value in CovData[0].items():
    print(f"{key} : {value}")

# Example 2: Sorting data based on a specific key (if applicable)
CovData.sort(key=itemgetter('country'))
for item in CovData:
    print(item['country'])

# Example 3: Print all rows and align data (if response has tabular-like structure)
n = max(len(str(x)) for row in CovData for x in row.values())  # Determine maximum column width
for row in CovData:
    print(' '.join(str(x).ljust(n) for x in row.values()))
'''
