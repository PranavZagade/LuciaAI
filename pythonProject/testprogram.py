"""
This script is a basic voice-controlled assistant named 'Jarvis'.
It can greet the user, recognize voice commands, and perform tasks like opening websites and telling the current time.
"""

import pyttsx3  # For text-to-speech conversion
import speech_recognition as sr  # For speech recognition
import datetime  # To fetch the current time
import webbrowser  # To open web pages

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')  # Use 'sapi5' TTS engine for Windows
voices = engine.getProperty('voices')  # Get the available voices
engine.setProperty('voice', voices[0].id)  # Set the desired voice (Male: voices[0], Female: voices[1])


def speak(audio):
    """
    Converts text to speech and speaks it.
    :param audio: Text to be spoken
    """
    engine.say(audio)
    engine.runAndWait()  # Process the queued text


def wishMe():
    """
    Greets the user based on the current time of day.
    """
    hour = int(datetime.datetime.now().hour)  # Get the current hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    # Personalized greeting
    speak("Please tell me how may I help you")


def takeCommand():
    """
    Listens to the user's voice and converts it to text.
    :return: User's query as a string
    """
    r = sr.Recognizer()  # Initialize the recognizer
    with sr.Microphone() as source:
        print("Say something!")  # Prompt the user
        audio = r.listen(source)  # Listen to the user's voice

    try:
        print("Recognizing...")  # Process the audio
        query = r.recognize_google(audio)  # Use Google's speech recognition
        print(f"User said: {query}\n")  # Print the recognized query
    except Exception as e:
        print("Say that again please...")  # Handle recognition errors
        return "None"  # Return "None" if the recognition fails
    return query


# Call the function to greet the user
wishMe()


def startCode():
    """
    Main loop to handle user commands and perform actions.
    """
    while True:
        query = takeCommand().lower()  # Convert the user's query to lowercase
        if 'open youtube' in query:
            webbrowser.open("youtube.com")  # Open YouTube
        elif 'open google' in query:
            webbrowser.open("google.com")  # Open Google
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")  # Open StackOverflow
        elif 'the time' in query:
            # Fetch and speak the current time
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")


# Start listening for commands
startCode()
