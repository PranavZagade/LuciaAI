import pyttsx3
import datetime
import speech_recognition as sr

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the voice property (use voices[33] if available, or change index as needed)
voices = engine.getProperty('voices')  # Get details of current voices
engine.setProperty('voice', voices[0].id)  # Default voice, change index for other voices

def speak(audio):
    """
    Speak out the provided text using the TTS engine.
    """
    engine.say(audio)
    engine.runAndWait()  # Without this, speech will not be audible.

def wishme():
    """
    Greet the user based on the current time.
    """
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("How can I assist you?")

def takeCommand():
    """
    Listen to the user's command through the microphone and recognize the text.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # Pause duration before stopping listening
        try:
            audio = r.listen(source)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')  # Recognize speech
            print(f"User said: {query}\n")
            return query
        except Exception as e:
            print("Could not understand your command. Please try again.")
            return "None"  # Return "None" for unrecognized input

# Main function execution
if __name__ == "__main__":
    wishme()  # Greet the user
    user_query = takeCommand()  # Get user input
    if user_query != "None":
        print(f"You said: {user_query}")  # Print recognized command
