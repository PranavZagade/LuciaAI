"""
This script uses the Alpha Vantage API to fetch intraday stock data for Tesla (TSLA).
The data includes open, high, low, close, and volume values for a specific time interval (60 minutes).
"""

import requests  # Import the requests library to handle HTTP requests

# Define the API endpoint URL
url = "https://alpha-vantage.p.rapidapi.com/query"

# Define the query parameters for the API request
querystring = {
    "interval": "60min",  # Time interval between data points
    "function": "TIME_SERIES_INTRADAY",  # Function to retrieve intraday data
    "symbol": "TSLA",  # Stock symbol (Tesla)
    "datatype": "json",  # Response format
    "output_size": "compact"  # Number of data points (compact: latest 100, full: entire history)
}

# Define the headers with RapidAPI credentials
headers = {
    "x-rapidapi-host": "alpha-vantage.p.rapidapi.com",  # API host
    "x-rapidapi-key": "cb12f5da9emsh4a615c4a900a1a8p12379cjsnc893378f0af6"  # Replace with your API key
}

# Send the GET request to the API
response = requests.request("GET", url, headers=headers, params=querystring)

# Parse the response JSON
data = response.json()

# Verify the type of the response (should be a dictionary)
print("Response Data Type:", type(data))

# Print the raw JSON response (optional for debugging)
# print("Raw Data:", data)

# Extract and display metadata
try:
    print("Last Refreshed:", data["Meta Data"]["3. Last Refreshed"])  # Last refreshed timestamp
except KeyError:
    print("Meta Data not found in the response.")

# Extract and display time series data for a specific timestamp
timestamp = "2021-12-13 20:00:00"  # Example timestamp
try:
    time_series = data["Time Series (60min)"][timestamp]
    print("Open Price:", time_series["1. open"])  # Open price
    print("High Price:", time_series["2. high"])  # High price
    print("Low Price:", time_series["3. low"])  # Low price
    print("Close Price:", time_series["4. close"])  # Close price
    print("Volume:", time_series["5. volume"])  # Volume
except KeyError:
    print(f"Time Series data not available for timestamp: {timestamp}")
