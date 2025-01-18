# Automated Media Control Script
# This script checks the status of various media services (Apple Music, Amazon Prime, Netflix)
# from a JSON file hosted on a URL and performs corresponding actions based on their status.

import time  # For adding delays
import requests  # For making HTTP GET requests
from playsound import playsound  # For playing sound files
import os  # For interacting with the operating system
from selenium import webdriver  # For automating browser actions

# URL of the JSON file
url = "http://storeonclouds.com/test1.json"

# Fetch initial data from the JSON file
resp = requests.get(url)
data = resp.json()


def refresh_data():
    """
    Refresh the global data by fetching the latest data from the JSON URL.
    """
    global data
    resp = requests.get(url)
    data = resp.json()


# Infinite loop to continuously monitor and act on the media service statuses
while True:
    # Extract the current statuses of the services
    result = data[0]['Apple_Music']
    result1 = data[1]['Amazon_Prime']
    result2 = data[2]['Netflix']

    # Counters to ensure actions are executed only once for each service
    count = 0
    count1 = 0
    count2 = 0

    # Check if Apple Music is "ON"
    if result == "ON":
        if count == 0:
            time.sleep(4)  # Add a delay before taking action
            playsound('song.wav')  # Play a sound
            count = count + 1  # Update the counter to avoid re-execution

    # Check if Amazon Prime is "ON"
    if result1 == "ON":
        if count1 == 0:
            os.system("open /Applications/PrimeVideo.app")  # Open the Amazon Prime Video app on macOS
            count1 = count1 + 1  # Update the counter

    # Check if Netflix is "ON"
    if result2 == "ON":
        if count2 == 0:
            # Open Netflix in a browser using Selenium
            driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and in PATH
            driver.get('https://www.netflix.com/title/81218396')  # Open the specific Netflix title
            count2 = count2 + 1  # Update the counter

    # Print the current statuses of the services
    print("Apple Music: " + data[0]['Apple_Music'])
    print("Amazon Prime: " + data[1]['Amazon_Prime'])
    print("Netflix: " + data[2]['Netflix'] + "\n")

    # Refresh the data from the JSON URL
    refresh_data()
