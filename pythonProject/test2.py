"""
A personal assistant program named Lucia that performs various tasks:
- Greeting the user
- Responding to voice commands
- Performing web searches
- Opening applications
- Playing music
- Sending emails
- Providing the current time
"""

import time  # For adding delays
import pyttsx3  # Text-to-speech conversion library
import speech_recognition as sr  # Speech recognition library
import datetime  # For date and time operations
import wikipedia  # To fetch summaries from Wikipedia
import webbrowser  # To open web pages
import os  # To interact with the operating system
import smtplib  # To send emails
from selenium import webdriver  # For automated browser control
from playsound import playsound  # To play audio files

# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[33].id)  # Set a specific voice (adjust index as needed)
time.sleep(10)  # Optional delay to ensure the engine initializes

def speak(audio):
    """
    Convert text to speech and play it.
    """
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    """
    Greet the user based on the current time of day.
    """
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Hey Pranav, How can I help you?")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

def takeCommand():
    """
    Listen to the user's voice input and convert it to text.
    Returns:
        str: The recognized text, or "None" if recognition fails.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # Adjust to control how long to pause before processing input
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Recognize speech in Indian English
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    """
    Send an email using SMTP.
    Args:
        to (str): Recipient's email address.
        content (str): The email content.
    """
    server = smtplib.SMTP('smtp.gmail.com', 587)  # Gmail's SMTP server
    server.ehlo()
    server.starttls()  # Upgrade to a secure connection
    server.login('abc@gmail.com', 'your-password')  # Replace with your credentials
    server.sendmail('anbemail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()  # Greet the user
    while True:
        query = takeCommand().lower()  # Convert user input to lowercase

        # Wikipedia search
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        # Open Amazon Prime Video
        elif 'open video' in query:
            speak("Enjoy Prime Video")
            os.system("open /Applications/PrimeVideo.app")
            time.sleep(5)
            os.system("pkill PrimeVideo")  # Close Prime Video
            speak("Closed Amazon Prime Video")
            time.sleep(5)
            os.system("open -a Music.app")

        # Open Apple Music
        elif 'open music' in query:
            os.system("open -a Music.app")

        # Open Google
        elif 'open google' in query:
            webbrowser.open("google.com")

        # Goodnight command
        elif 'goodnight' in query:
            speak("Good Night Sir")
            speak("Alarm and schedule for tomorrow updated. Closing Lucia program.")
            break  # Exit the loop

        # Open YouTube
        elif 'open youtube' in query:
            driver = webdriver.Chrome()
            driver.get('https://www.youtube.com/')

        # Respond to greeting
        elif 'hey lucia' in query:
            speak("Hello Pranav, How can I help you?")

        # Play a specific song
        elif 'play bts dynamite' in query:
            speak("Playing BTS dynamite from Apple Music")
            playsound('dynamite.wav')

        # Provide the current time
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        # Open Visual Studio Code
        elif 'open code' in query:
            codePath = "YOUR PATH"
            os.startfile(codePath)

        # Send an email
        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "youremail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am unable to send the email.")
