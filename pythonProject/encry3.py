# Base64 Encoding a Message
# This script demonstrates how to encode a plain text message into Base64 format.

import base64  # Import the base64 module for encoding and decoding

# Original message
message = "Hello World"

# Convert the message to bytes (required for Base64 encoding)
message_bytes = message.encode('ascii')

# Encode the byte message into Base64
base64_bytes = base64.b64encode(message_bytes)

# Convert the Base64-encoded bytes back to a string
base64_message = base64_bytes.decode('ascii')

# Print the Base64-encoded message
print(base64_message)
