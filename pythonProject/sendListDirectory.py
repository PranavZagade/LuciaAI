"""
This script demonstrates how to send data using the POST method to a server-side script (check_req_data.php).
It retrieves a list of files and directories from a specified path, converts the list into a single string,
and sends it as POST data.
"""

import requests  # For making HTTP requests
import os  # For interacting with the operating system

# Define the path to list files and directories
path = "/Users/pranavzagade/Downloads"  # Replace with the desired path on your system

# Get the list of all files and directories in the specified path
dir_list = os.listdir(path)

# Print the retrieved list for debugging
print("Files and directories in '", path, "' :")
print(dir_list)

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
        str += i + ','  # Append each element and add a comma as a separator
    return str.strip(',')  # Remove the trailing comma

# Define the URL for the POST request
url = "http://storeonclouds.com/check_req_data.php"

# Prepare the data payload for the POST request
data = {'listname': convertList(dir_list)}

# Send the POST request with the data
response = requests.post(url, data)

# Print the server response
print("Response Status Code:", response.status_code)  # HTTP status code (e.g., 200 for success)
print("Response Text:", response.text)  # Response content
