# List Files and Directories in a Given Path
# This script retrieves and displays all files and directories in a specified path.

import os  # Import the os module for interacting with the operating system

# Define the path to the directory
path = "/Users/pranavzagade/Documents/StoreOnClouds"  # Replace with your desired path

# Get the list of all files and directories in the specified path
dir_list = os.listdir(path)

# Display the path and its contents
print("Files and directories in '", path, "' :")
print(dir_list)  # Print the list of files and directories
print(type(dir_list))  # Print the type of the variable (list)
