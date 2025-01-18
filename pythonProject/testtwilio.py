from twilio.rest import Client

# Your Account SID and Auth Token (hidden for security)
account_sid = "ACxxxxxx...xxxx"  # Replace with your actual SID
auth_token = "xxxxxxxxxx...xxxx"  # Replace with your actual Auth Token

# Initialize the Twilio client
client = Client(account_sid, auth_token)

# Fetch a list of transcriptions (limit to 20)
transcriptions = client.transcriptions.list(limit=20)

# Print transcription details
print("List of Transcriptions:")
for record in transcriptions:
    print(f"Transcription SID: {record.sid}")  # Display only the transcription SID
