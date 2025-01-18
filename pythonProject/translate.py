"""
Google Translate
By Google Cloud | Text Analysis
"""

import requests  # Importing the requests library to handle HTTP requests

# Define the API endpoint for Google Translate
url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

# Set the target language code (e.g., 'fr' for French) and the text to translate
language_encoded = "fr"  # Language code for French
query = "Good Morning"  # Text to be translated

# Payload for the POST request with the text to be translated and language settings
payload = f"q={query}&target={language_encoded}&source=en"

# Headers for the POST request, including content type and API credentials
headers = {
    'content-type': "application/x-www-form-urlencoded",  # Content type for the request
    'accept-encoding': "application/gzip",  # Accept compressed response
    'x-rapidapi-host': "google-translate1.p.rapidapi.com",  # API host
    'x-rapidapi-key': "cb12f5da9emsh4a615c4a900a1a8p12379cjsnc893378f0af6"  # API key for authentication
}

# Send the POST request to the API endpoint
response = requests.request("POST", url, data=payload, headers=headers)

# Parse the JSON response returned by the API
data = response.json()

# Print the raw response text (debugging or verification purpose)
print(response.text)

# Extract and print the translated text from the API response
print(data["data"]["translations"][0]['translatedText'])  # Translated text output
