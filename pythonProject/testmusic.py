"""
This script defines a function that plays an audio file using the `playsound` library.
The audio file ('dynamite.wav') is played when the function `my_function` is called.
"""

# Import the `playsound` function from the `playsound` library
from playsound import playsound

# Define a function to play the audio file
def my_function():
    """
    This function plays the 'dynamite.wav' audio file.
    Ensure the file exists in the same directory or provide the full file path.
    """
    playsound('dynamite.wav')  # Play the audio file

# Call the function to play the sound
my_function()
