"""
This script sends a large block of text as a GET request to a specified URL.
The `requests` library is used to make the HTTP request. 
The server-side script `check_req_data.php` will receive and process the data.
"""

import requests  # Import the requests library for making HTTP requests

# Define the text data to be sent
text = (
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
    "Ornare suspendisse sed nisi lacus sed viverra tellus in. Cras ornare arcu dui vivamus arcu felis bibendum. "
    "Interdum posuere lorem ipsum dolor sit amet. Sit amet massa vitae tortor condimentum lacinia. "
    "Sed augue lacus viverra vitae congue. Varius quam quisque id diam vel quam elementum. "
    "Morbi tristique senectus et netus et malesuada fames ac. Mus mauris vitae ultricies leo integer malesuada nunc vel. "
    "Justo nec ultrices dui sapien eget mi proin. Mattis molestie a iaculis at erat pellentesque adipiscing."
)

# Define an additional text field
text1 = "pranav"

# Define the target URL and append the query parameter
url = f"http://storeonclouds.com/check_req_data.php?test={text}&name={text1}"

# Send the GET request to the URL
response = requests.get(url)

# Print the response from the server
print("Response Status Code:", response.status_code)
print("Response Text:", response.text)
