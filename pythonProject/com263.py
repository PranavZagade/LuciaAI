# Virtual Assistant: "Lucia"
# This script initializes a virtual assistant named Lucia. It uses speech synthesis and recognition
# to interact with the user, greet them based on the time of day, and execute basic commands like
# opening websites or informing the user about tasks.

import time
import xlrd  # For working with Excel files (not used in this code, can be removed if unnecessary)
import pyttsx3  # For text-to-speech functionality
import datetime  # For fetching the current time
import speech_recognition as sr  # For speech recognition
import os  # For operating system commands
import webbrowser  # For opening websites
import smtplib  # For sending emails (not used in this code, can be removed if unnecessary)
import wikipedia  # For fetching information from Wikipedia (not used in this code, can be removed if unnecessary)
import requests  # For making HTTP requests (not used in this code, can be removed if unnecessary)
from selenium import webdriver  # For web automation (not used in this code, can be removed if unnecessary)

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Print all available voices to identify valid voice indices
for index, voice in enumerate(voices):
    print(f"Voice {index}: {voice.name}")

# Set a valid voice index (Change the index as needed to match your desired voice)
engine.setProperty('voice', voices[135].id)  # Make sure the index exists, or this may cause an error

# Add a short delay
time.sleep(5)

# Function for speaking the provided text
def speak(audio):
    """
    Convert text to speech and output it using the selected voice.
    
    Args:
        audio (str): Text to be spoken.
    """
    engine.say(audio)
    engine.runAndWait()  # Without this, the speech will not be audible

# Function to greet the user based on the current time
def wishMe():
    """
    Greet the user based on the current hour of the day.
    """
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning Pranav, I am Lucia")
        speak("your personal Artificial Intelligence")
        speak("How can I help you?")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
        speak("How can I help you?")

    else:
        speak("Hello Pranav, I am Lucia")
        speak("your personal Artificial Intelligence")
        speak("How can I help you?")

# Function to capture voice input from the user
def takeCommand():
    """
    Capture and recognize speech input from the user.
    
    Returns:
        str: Recognized text from the user's speech.
    """
    r = sr.Recognizer()  # Initialize the recognizer
    with sr.Microphone() as source:  # Use the default microphone as the input source
        print("Listening...")
        r.pause_threshold = 1  # Wait time before processing the input
        audio = r.listen(source)  # Capture the audio

    try:
        print("Recognizing...")
        # Use Google's speech recognition to convert audio to text
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")  # Print the recognized query

    except Exception as e:
        print(e)
        print("Say that again please...")  # Prompt user to speak again if recognition fails
        return "None"  # Return "None" if speech is not recognized
    return query

# Main function to start the virtual assistant
if __name__ == "__main__":
    wishMe()  # Greet the user
    while True:
        query = takeCommand().lower()  # Capture and process user commands

        # Command to open a project webpage
        if 'open project' in query:
            os.system("open \"\" http://pranavzagadeproductions.in/project.html")
            time.sleep(90)  # Pause for 90 seconds after opening the webpage

        # Command to open a quiz webpage
        elif 'open quiz' in query:
            os.system("open \"\" http://pranavzagadeproductions.in/Comtest.php")
