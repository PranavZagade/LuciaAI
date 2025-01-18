"""
This is a voice-controlled assistant program that can perform tasks such as searching Wikipedia, opening websites or applications, and providing the current time.
"""

# Import necessary modules
import time  # For sleep and time-related operations
import pyttsx3  # For text-to-speech conversion
import speech_recognition as sr  # For speech recognition
import datetime  # For handling date and time
import wikipedia  # For retrieving information from Wikipedia
import webbrowser  # For opening web pages
import os  # For executing system commands
from selenium import webdriver  # For automated browser interactions
from playsound import playsound  # For playing audio files

# Initialize the pyttsx3 engine for text-to-speech
engine = pyttsx3.init()
voices = engine.getProperty('voices')  # Get the list of available voices
engine.setProperty('voice', voices[33].id)  # Set a specific voice (adjust index as needed)
time.sleep(10)  # Wait for 10 seconds before proceeding

# Function to make the assistant speak
def speak(audio):
    """
    Converts text into speech.
    """
    engine.say(audio)
    engine.runAndWait()  # Ensures the audio is played

# Function to greet the user based on the time of the day
def wishMe():
    """
    Greets the user based on the current time.
    """
    hour = int(datetime.datetime.now().hour)  # Get the current hour
    if hour >= 0 and hour < 12:
        speak("Hey Pranav")
        speak("How can I help you?")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

# Function to take voice input from the user
def takeCommand():
    """
    Listens to the user's voice input and converts it to text.
    Returns:
        str: The recognized text or 'None' if recognition fails.
    """
    r = sr.Recognizer()  # Initialize the recognizer
    with sr.Microphone() as source:  # Use the microphone as the audio source
        print("Listening...")
        r.pause_threshold = 1  # Adjust pause threshold for recognition
        audio = r.listen(source)  # Listen to the audio input

    try:
        print("Recognizing...")
        # Recognize speech using Google's speech recognition API
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"  # Return 'None' if recognition fails
    return query

# Main program execution
if __name__ == "__main__":
    wishMe()  # Call the greeting function
    while True:
        query = takeCommand().lower()  # Take user input and convert to lowercase

        # Task: Search Wikipedia
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")  # Remove the word 'wikipedia' from the query
            results = wikipedia.summary(query, sentences=2)  # Fetch summary from Wikipedia
            speak("According to Wikipedia")
            print(results)  # Print the result
            speak(results)  # Speak the result

        # Task: Open Prime Video
        elif 'open video' in query:
            speak("Enjoy Prime Video")
            os.system("open /Applications/PrimeVideo.app")  # Open Prime Video application
            time.sleep(5)  # Wait for 5 seconds
            os.system("pkill PrimeVideo")  # Close Prime Video application
            speak("Closed Amazon Prime Video")
            time.sleep(5)
            os.system("open -a Music.app")  # Open Music application

        # Task: Open Music
        elif 'open music' in query:
            os.system("open -a Music.app")  # Open Music application

        # Task: Open Google
        elif 'open google' in query:
            webbrowser.open("google.com")  # Open Google in the web browser

        # Task: Respond to 'Goodnight'
        elif 'goodnight' in query:
            speak("Good Night Sir")
            time.sleep(1)
            speak("Alarm and schedule for tomorrow are updated")
            speak("Lucia about to close program")
            speak("Program closed successfully")
            break  # Exit the program loop

        # Task: Open YouTube
        elif 'open youtube' in query:
            driver = webdriver.Chrome()  # Initialize a Chrome browser
            driver.get('https://www.youtube.com/')  # Open YouTube

        # Task: Greet when addressed as 'Hey Lucia'
        elif 'hey lucia' in query:
            speak("Hello Pranav")
            time.sleep(2)
            speak("How can I help you?")

        # Task: Provide the current time
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")  # Get the current time
            speak(f"Sir, the time is {strTime}")  # Speak the current time
