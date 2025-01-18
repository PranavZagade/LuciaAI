import time  # Importing time module for delays
import webbrowser  # Importing webbrowser module to open URLs in the default browser
import requests  # Importing requests library to handle HTTP requests

# Define the URL for fetching the JSON data
url = "http://storeonclouds.com/testapp/test1.json"

# Fetch initial data from the URL
resp = requests.get(url)
data = resp.json()  # Parse the JSON response

# Function to refresh data by re-fetching from the URL
def refresh_data():
    global data
    resp = requests.get(url)  # Send a GET request to the URL
    data = resp.json()  # Update the global data variable with the new JSON response

# Start the monitoring loop
while True:
    result = data[0]['Apple_Music']  # Check the 'Apple_Music' key in the first item of the JSON data
    count = 0  # Counter to ensure the action is performed only once

    # Check if 'Apple_Music' is set to "ON"
    if result == "ON":
        if count == 0:
            time.sleep(4)  # Wait for 4 seconds
            # Open a YouTube video in the default browser
            webbrowser.open("https://www.youtube.com/watch?v=ApXoWvfEYVU#t=25s&ab_channel=PostMaloneVEVO&autoplay=1")
            count = count + 1  # Increment the counter
            break  # Exit the loop after opening the video

    # Print the status of 'Apple_Music' for debugging or monitoring
    print("Youtube Music : " + data[0]['Apple_Music'])

    # Refresh the data by re-fetching from the URL
    refresh_data()
