import requests
from urllib.parse import urlencode  # For URL encoding

# Define the text and additional parameter to send
text1 = "pranav zagade"
text = (
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore "
    "et dolore magna aliqua. Ornare suspendisse sed nisi lacus sed viverra tellus in. Cras ornare arcu dui "
    "vivamus arcu felis bibendum. Interdum posuere lorem ipsum dolor sit amet. Sit amet massa vitae tortor "
    "condimentum lacinia. Sed augue lacus viverra vitae congue. Varius quam quisque id diam vel quam elementum. "
    "Morbi tristique senectus et netus et malesuada fames ac. Mus mauris vitae ultricies leo integer malesuada "
    "nunc vel. Justo nec ultrices dui sapien eget mi proin. Mattis molestie a iaculis at erat pellentesque adipiscing. "
    "IS THIS THE END"
)

# Define the URL
base_url = "http://storeonclouds.com/check_req_data.php"

# Encode the query parameters
params = {"test": text1, "description": text}  # Add additional parameters if needed
encoded_params = urlencode(params)

# Concatenate the URL with encoded parameters
final_url = f"{base_url}?{encoded_params}"

# Send the GET request
response = requests.get(final_url)

# Print the server response
print("Status Code:", response.status_code)  # HTTP status code (e.g., 200 for success)
print("Response Text:", response.text)       # Response content
