import requests  # Importing the requests library for making HTTP requests

# Define the base URL for the weather API
url = "https://weatherapi-com.p.rapidapi.com/current.json"

# Define the query string with location information
querystring = {"q": "q=tempe Arizona"}  # Specify the city and state

# Define the headers, including the API host and API key
headers = {
    'x-rapidapi-host': "weatherapi-com.p.rapidapi.com",
    'x-rapidapi-key': "API_KEY"
}

# Make a GET request to the weather API with the headers and query string
response = requests.request("GET", url, headers=headers, params=querystring)

# Print the raw JSON response (optional, for debugging purposes)
print(response.text)

# Parse the JSON response into a Python dictionary
data = response.json()

# Print the data type to confirm it's a dictionary
print(type(data))

# Access the current temperature in Celsius from the parsed data
print(data["current"]['temp_c'])
