"""
This script is a simple voice assistant using Python.
Features include greeting the user, opening websites (YouTube, Google, StackOverflow), 
and reporting the current time. A GUI button triggers the assistant loop.
"""

import pyttsx3  # Text-to-speech conversion
import speech_recognition as sr  # Speech recognition
import datetime  # For fetching current time
import webbrowser  # For opening web pages
import tkinter  # For creating a simple GUI

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')  # Use 'sapi5' TTS engine for Windows
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Set the voice (0 = Male, 1 = Female)


def speak(audio):
    """
    Converts text to speech and speaks it.
    :param audio: Text to be spoken
    """
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    """
    Greets the user based on the current time of day.
    """
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Please tell me how may I help you")


def takeCommand():
    """
    Listens to the microphone input and converts it to text.
    :return: User query as a string
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)  # Using Google's speech recognition
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")  # If recognition fails
        return "None"
    return query


def inTheLoop():
    """
    Main loop for handling user commands.
    """
    while True:
        query = takeCommand().lower()  # Convert user input to lowercase
        if 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")


if __name__ == "__main__":
    # Create a simple GUI window using tkinter
    window_main = tkinter.Tk(className='Voice Assistant')  # Window title
    window_main.geometry("400x200")  # Window size (width x height)

    # Greet the user
    wishMe()

    # Add a button to start the voice assistant loop
    button_submit = tkinter.Button(window_main, text="Activate Assistant", command=inTheLoop)
    button_submit.pack()  # Place the button in the window

    # Start the main GUI loop
    window_main.mainloop()
