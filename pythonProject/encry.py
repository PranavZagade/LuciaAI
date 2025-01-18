# Encrypt and Decrypt Messages Using Fernet (Symmetric Encryption)
# This script demonstrates how to use the Fernet module from the cryptography library
# to securely encrypt and decrypt a message. It also shows how to save and retrieve a secret key.

from cryptography.fernet import Fernet

# Uncomment this section if you need to generate and save a new key
'''
# Generate a new secret key
key = Fernet.generate_key()
print(key)

# Save the generated key to a file
with open('key.key', 'wb') as file:
    file.write(key)
'''

# Load the secret key from the file
with open('key.key', 'rb') as file:
    key = file.read()  # Read the key as bytes
print(f"Key: {key}")

# Message to be encrypted (convert it to bytes)
message = "Hello World, How are you?".encode()
print(f"Original Message (Bytes): {message}")

# Create a Fernet object using the loaded key
f = Fernet(key)

# Encrypt the message
encrypted = f.encrypt(message)
print(f"Encrypted Message: {encrypted}")

# Decrypt the message
decrypted = f.decrypt(encrypted)
print(f"Decrypted Message (Bytes): {decrypted}")

# Convert the decrypted bytes back to a string
original_message = decrypted.decode()
print(f"Original Message (String): {original_message}")
