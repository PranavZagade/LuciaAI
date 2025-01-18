
"""
Virtual Assistant Script

This script implements a virtual assistant capable of performing various tasks, including:
1. Greeting the user based on the time of day.
2. Voice-based interaction to handle commands.
3. Searching Wikipedia and reading results aloud.
4. Performing Google searches using RapidAPI and opening results in a browser.
5. Retrieving real-time stock prices via Alpha Vantage API.
6. Sending grocery list updates via Twilio SMS.
7. Opening commonly used applications and websites.

Modules used:
- pyttsx3: Text-to-speech conversion
- speech_recognition: Capturing and recognizing user voice input
- wikipedia: Fetching summaries for user queries
- xlrd: Reading data from Excel files
- requests: Making API calls for stock prices and Google searches
- selenium: Automating browser actions
- os/webbrowser: Opening local applications and websites
"""

# Import required libraries and modules
import time  # For adding delays
import xlrd  # For reading data from Excel files
import pyttsx3  # For text-to-speech conversion
import datetime  # For fetching current time
import speech_recognition as sr  # For recognizing speech
import os  # For interacting with the operating system
import webbrowser  # For opening web pages
import smtplib  # For sending emails
import wikipedia  # For searching Wikipedia
from twilio.rest import Client  # For sending messages using Twilio API
import requests  # For making HTTP requests
from selenium import webdriver  # For automating browser actions

# Twilio credentials (replace with actual credentials)
account_sid = "Your SID"
auth_token = "Your Auth Token"

# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')  # Fetch available voices

# Print all available voices for reference
for index, voice in enumerate(voices):
    print(f"Voice {index}: {voice.name}")

# Set a specific voice for the assistant
engine.setProperty('voice', voices[5].id)  # Adjust the index as needed

def speak(audio):
    """
    Convert the given text to speech.
    """
    engine.say(audio)
    engine.runAndWait()  # Execute speech synthesis

def wishMe():
    """
    Greet the user based on the current time of day.
    """
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Hello Pranav")
        speak("How can I help you?")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
        speak("How can I assist you?")
    else:
        speak("Good Evening!")
        speak("Hello, how can I assist you tonight?")

def takeCommand():
    """
    Listen to and recognize the user's voice commands.
    Returns:
        str: The recognized command or "None" if recognition fails.
    """
    r = sr.Recognizer()  # Initialize the recognizer
    with sr.Microphone() as source:  # Use the default microphone as input
        print("Listening...")
        r.pause_threshold = 1  # Adjust for speech gaps
        try:
            audio = r.listen(source)  # Capture audio input
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')  # Recognize speech using Google API
            print(f"User said: {query}\n")  # Print the recognized text
        except Exception as e:
            print("Say that again please...")  # Handle recognition errors
            return "None"
    return query

def get_stocks_price(ticker):
    """
    Fetch stock price details for the given ticker symbol.
    Args:
        ticker (str): Stock ticker symbol.
    """
    url = "https://alpha-vantage.p.rapidapi.com/query"
    querystring = {
        "interval": "60min", 
        "function": "TIME_SERIES_INTRADAY", 
        "symbol": ticker, 
        "datatype": "json", 
        "output_size": "compact"
    }
    headers = {
        'x-rapidapi-host': "alpha-vantage.p.rapidapi.com",
        'x-rapidapi-key': "Your_RapidAPI_Key"  # Replace with your RapidAPI key
    }
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()

    # Fetch and speak relevant stock details
    last_refreshed = list(data["Time Series (60min)"].keys())[0]
    stock_data = data["Time Series (60min)"][last_refreshed]
    speak(f"Opening Price: {stock_data['1. open']} dollars.")
    speak(f"Highest Price: {stock_data['2. high']} dollars.")
    speak(f"Lowest Price: {stock_data['3. low']} dollars.")
    speak(f"Closing Price: {stock_data['4. close']} dollars.")
    speak(f"Volume: {stock_data['5. volume']} shares traded.")

# Main logic of the assistant
if __name__ == "__main__":
    wishMe()  # Greet the user

    while True:
        query = takeCommand().lower()  # Capture user command

        # Handle Wikipedia searches
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        # Handle Google search activation
        elif 'activate google' in query:
            speak("Google search activated. What do you want to search?")
            search_query = takeCommand().lower()
            url = f"https://google-search3.p.rapidapi.com/api/v1/search/q={search_query}&num=100"
            headers = {
                'x-user-agent': "desktop",
                'x-proxy-location': "US",
                'x-rapidapi-host': "google-search3.p.rapidapi.com",
                'x-rapidapi-key': "Your_RapidAPI_Key"  # Replace with your RapidAPI key
            }
            response = requests.get(url, headers=headers)
            data = response.json()
            title = data["results"][0]["title"]
            link = data["results"][0]["link"]
            speak(f"Result: {title}")
            speak("Do you want to open the page?")
            opt = takeCommand().lower()
            if opt == "yes":
                driver = webdriver.Chrome()
                driver.get(link)
                time.sleep(10)

        # Add items to the grocery list via Twilio
        elif 'add grocery list' in query:
            speak("What do you want to add?")
            item = takeCommand().lower()
            message = f"Hello Pranav, your grocery list: {item}"
            client = Client(account_sid, auth_token)
            client.messages.create(to="+18458668681", from_="+15407016004", body=message)
            speak("Item added to your grocery list.")

        # Fetch stock information
        elif 'search stocks' in query:
            loc = "Stocks.xls"  # Path to the Excel file
            wb = xlrd.open_workbook(loc)
            sheet = wb.sheet_by_index(0)
            speak("Which company's stock do you want to search for?")
            company_name = takeCommand().lower()
            for i in range(sheet.nrows):
                if company_name in sheet.cell_value(i, 0).lower():
                    ticker = sheet.cell_value(i, 1)
                    get_stocks_price(ticker)

        # Handle general commands
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open music' in query:
            os.system("open -a Music.app")
        elif 'open prime video' in query:
            os.system("open /Applications/PrimeVideo.app")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
