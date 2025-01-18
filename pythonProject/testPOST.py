"""
This script sends a large string of text data to a server using the POST method.
The data is sent to a specified URL (`check_req_data.php`) and the response is printed.
"""

import requests  # For sending HTTP requests

# Define a large string of text (1000+ words) to be sent
dir_list = (
    "Lorem ipsum dolor sit amet, an debet soluta ius, qui et nobis dignissim. "
    "An mel quis comprehensam. In accusamus incorrupte signiferumque est, dicat homero propriae mei at. "
    "Eam sumo mazim labore ut, te praesent scriptorem vis. Veri officiis tacimates at qui. "
    "Ea sea modo appetere eleifend, eos facilisi torquatos ex. "
    * 20  # Repeating the text multiple times to reach 1000+ words
)

# Define the target URL for the POST request
url = "http://storeonclouds.com/check_req_data.php"

# Prepare the data payload for the POST request
data = {'listname': dir_list}  # 'listname' is the key expected by the server

# Send the POST request with the data payload
r = requests.post(url, data)

# Print the response from the server
print("Response Status Code:", r.status_code)  # HTTP status code
print("Response Text:", r.text)  # Server response body
