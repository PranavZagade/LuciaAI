'''
CODE DESCRIPTION:
This Python script demonstrates how to encrypt and decrypt a password using
the cryptography library's Fernet encryption. The encryption process converts
the password into a secure, unreadable format, and the decryption process restores
it to its original form.
'''
from cryptography.fernet import Fernet

# Generate a key for encryption/decryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Password to encrypt
password = "MyAdmin@123"

# Encrypt the password
encrypted_password = cipher_suite.encrypt(password.encode())
# Convert encrypted password from bytes to string
encrypted_password_str = encrypted_password.decode('utf-8')
print(f"Encrypted password (string): {encrypted_password_str}")

# Decrypt the password
decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
print(f"Decrypted password: {decrypted_password}")
