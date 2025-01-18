"""
This script captures audio input from the microphone and performs speech-to-text conversion using the SpeechRecognition library.
"""

import speech_recognition as sr  # Import the SpeechRecognition library

# Create an instance of the Recognizer class
r = sr.Recognizer()

# Use the microphone as the audio source
with sr.Microphone() as source:
    print("Say something!")  # Prompt the user to speak

    # Capture audio input from the microphone
    audio = r.listen(source)

try:
    # Use Google's speech recognition to convert audio to text
    text = r.recognize_google(audio)  # Perform speech-to-text
    print("You said:", text)  # Print the recognized text

except sr.UnknownValueError:
    # Handle cases where the speech was unintelligible
    print("Google Speech Recognition could not understand audio")

except sr.RequestError as e:
    # Handle cases where there are issues connecting to the recognition service
    print(f"Could not request results from Google Speech Recognition service; {e}")
