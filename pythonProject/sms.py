"""
This script uses the Twilio API to send an SMS message.
Replace placeholders with your actual Twilio credentials and phone numbers.
"""

from twilio.rest import Client  # Import the Twilio client library

# Your Twilio Account SID and Auth Token (replace with your own credentials)
account_sid = "___"  # Replace with your Twilio Account SID
auth_token = "_______"  # Replace with your Twilio Auth Token

# Initialize the Twilio client
client = Client(account_sid, auth_token)

# Define the message content
mes = "Hello Pranav, Your reminder!"  # Customize the message as needed

# Send the SMS message
message = client.messages.create(
    to="+1XXXXXXXXXX",  # Replace with the recipient's phone number
    from_="+1540XXXXXXX",  # Replace with your Twilio phone number
    body=mes  # Message content
)

# Uncomment the following line to print the message SID for confirmation
# print(message.sid)
