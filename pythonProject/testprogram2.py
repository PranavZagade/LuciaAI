"""
This script creates a simple GUI (Graphical User Interface) using Tkinter, a Python library for GUI development.
It demonstrates creating a window, adding a button, and handling button click events.
"""

# Import the tkinter module
import tkinter

# Create the main application window
window_main = tkinter.Tk(className='Tkinter - TutorialKart')  # Set the title of the window
window_main.geometry("400x200")  # Set the size of the window to 400x200 pixels


# Define the function to be executed when the button is clicked
def printMessage():
    """
    This function prints a message to the console when called.
    """
    print('You clicked Submit button!')


# Create a button and associate it with the `printMessage` function
button_submit = tkinter.Button(window_main, text="Submit", command=printMessage)

# Add the button to the window and position it
button_submit.pack()

# Run the application's main loop to display the window
window_main.mainloop()
