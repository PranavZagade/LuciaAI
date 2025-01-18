"""
This script demonstrates how to use the `webbrowser` module and the `pywhatkit` library to open YouTube videos.
The script opens a specific YouTube video using `webbrowser` and optionally with `pywhatkit`.
"""

import pywhatkit  # Library for automating tasks like playing YouTube videos
import webbrowser  # Module to interact with the default web browser

# Open a specific YouTube video using the webbrowser module
# This URL includes a specific timestamp (`t=25s`) and autoplay enabled
webbrowser.open("https://www.youtube.com/watch?v=ApXoWvfEYVU#t=25s&ab_channel=PostMaloneVEVO&autoplay=1")

# Uncomment the following lines to use pywhatkit for playing YouTube videos:

# Open a YouTube video using pywhatkit with a specific start time and autoplay
# pywhatkit.playonyt("https://youtu.be/ApXoWvfEYVU?t=30&autoplay=1")

# Open a YouTube video using pywhatkit with another timestamp
# pywhatkit.playonyt("https://www.youtube.com/watch?v=ApXoWvfEYVU#t=1m30s&ab_channel=PostMaloneVEVO")

