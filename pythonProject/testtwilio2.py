import os
from twilio.rest import Client

# Use environment variables to securely store credentials
# Replace `TWILIO_ACCOUNT_SID` and `TWILIO_AUTH_TOKEN` with your actual environment variable names
account_sid = os.getenv("TWILIO_ACCOUNT_SID", "ACxxxxxx...xxxx")  # Hidden for security
auth_token = os.getenv("TWILIO_AUTH_TOKEN", "xxxxxxxxxx...xxxx")  # Hidden for security

# Initialize the Twilio client
client = Client(account_sid, auth_token)

# Fetch a specific transcription using its SID
transcription_sid = "TRxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # Replace with your transcription SID
transcription = client.transcriptions(transcription_sid).fetch()

# Print the transcription text
print(f"Transcription Text: {transcription.transcription_text}")
