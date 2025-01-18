"""
This program lists all files and directories in a specified path, 
converts the directory list into a single string, and adds a delimiter between items.
"""

import os  # Importing the os module to interact with the operating system

# Define the path to list files and directories
path = "/Users/pranavzagade/Downloads"  # Replace with your desired directory path

# Get the list of all files and directories in the specified path
dir_list = os.listdir(path)

# Display the list of files and directories
print("Files and directories in '", path, "' :")
print(dir_list)

# Define a function to convert a list into a single string
def convertList(list1):
    """
    Convert a list of strings into a single concatenated string.

    Args:
        list1 (list): List of strings to convert.

    Returns:
        str: Concatenated string of all list elements.
    """
    str = ''  # Initialize an empty string
    for i in list1:  # Iterate through the list
        str += i  # Add each element of the list to the string
    return str

# Initialize variables
str = ''  # String to hold concatenated list elements
charToAdd = "%"  # Delimiter to add between elements
count = 0  # Counter for the number of elements

# Iterate through the list of directory contents
for i in dir_list:
    str += i  # Add each directory or file name to the string
    str += charToAdd  # Add the delimiter after each name
    count += 1  # Increment the counter

# Print the final concatenated string with delimiters
print(str)

# Split the concatenated string back into a list using the delimiter
print(str.split('%'))

# Print the total count of items
print(count)
