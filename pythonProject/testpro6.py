"""
This script initializes the pyttsx3 text-to-speech engine, modifies its voice and rate properties, 
and speaks a Spanish greeting "buenas noches" (Good Night).
"""

# Import required libraries
import time  # For adding sleep delays
import pyttsx3  # For text-to-speech conversion
import datetime  # To handle date and time operations (not used in this snippet)
import speech_recognition as sr  # For speech recognition (not used in this snippet)
import os  # To interact with the operating system (not used in this snippet)
import webbrowser  # To open web pages (not used in this snippet)
import smtplib  # To send emails (not used in this snippet)
import wikipedia  # For Wikipedia summaries (not used in this snippet)
from twilio.rest import Client  # For sending messages using Twilio (not used in this snippet)
import requests  # For making HTTP requests (not used in this snippet)
from selenium import webdriver  # For automating web browsers (not used in this snippet)

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Get details of the available voices
voices = engine.getProperty('voices')  # List of available voices
engine.setProperty('voice', voices[33].id)  # Set a specific voice (voice[33])

# Adjust the speech rate
rate = engine.getProperty('rate')  # Get the current speaking rate
print(rate)  # Print the current rate (default is usually 200)
engine.setProperty('rate', 200)  # Set a new speaking rate (200 is default)

# Delay to ensure audio plays smoothly
time.sleep(5)

# Define a function to speak the text
def speak(audio):
    """
    Converts text to speech and speaks it.
    :param audio: The text to be spoken
    """
    engine.say(audio)  # Queue the text to be spoken
    engine.runAndWait()  # Process the queued text

# Call the speak function to say "buenas noches"
speak("buenas noches")  # Say "Good Night" in Spanish
