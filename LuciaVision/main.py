# Simple Login Form Using Tkinter
# This script creates a basic GUI login form with fields for entering a username and password.
# When the "LOGIN" button is pressed, the entered data is printed to the console.

import tkinter as tk  # Import the Tkinter library for GUI development

# Function to handle the "LOGIN" button click
def submit_data():
    # Get the values entered in the username and password fields
    username_entry = entry_username.get()
    password_entry = entry_password.get()
    # Print the entered username and password to the console
    print(f'Username: {username_entry}, Password: {password_entry}')

# Create the main application window
root = tk.Tk()
root.title('MacBook Air - 1')  # Set the title of the window

# Create a frame to hold the form elements
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)  # Add padding around the frame

# Create and position the label for the "Username" field
label_username = tk.Label(frame, text='Username')
label_username.grid(row=0, column=0, padx=5, pady=5, sticky='w')  # Align label to the left

# Create and position the entry field for the username
entry_username = tk.Entry(frame)
entry_username.grid(row=0, column=1, padx=5, pady=5, sticky='w')

# Create and position the label for the "Password" field
label_password = tk.Label(frame, text='Password')
label_password.grid(row=1, column=0, padx=5, pady=5, sticky='w')  # Align label to the left

# Create and position the entry field for the password
entry_password = tk.Entry(frame, show='*')  # Use '*' to mask password input
entry_password.grid(row=1, column=1, padx=5, pady=5, sticky='w')

# Create and position the "LOGIN" button
submit_button = tk.Button(frame, text='LOGIN', command=submit_data)
submit_button.grid(row=2, column=1, padx=5, pady=5, sticky='e')  # Align button to the right

# Start the main event loop for the Tkinter application
root.mainloop()
