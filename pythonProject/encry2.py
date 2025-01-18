import binascii
from Crypto.Cipher import AES
from Crypto import Random
import base64
import json

def my_encrypt(data, passphrase):
    """
    Encrypt data using AES-256-CBC with a randomly generated IV.
    
    Args:
        data (str): The plaintext data to encrypt.
        passphrase (str): The passphrase in hex format, generated with 'openssl rand -hex 32'.
        
    Returns:
        str: Base64-encoded JSON string containing the IV and encrypted data.
    """
    try:
        # Convert the passphrase from hex to bytes
        key = binascii.unhexlify(passphrase)
        
        # Padding function to ensure data length is a multiple of 16 bytes
        pad = lambda s: s + chr(16 - len(s) % 16) * (16 - len(s) % 16)
        
        # Generate a random 16-byte IV
        iv = Random.get_random_bytes(16)
        
        # Initialize the AES cipher in CBC mode with the generated IV
        cipher = AES.new(key, AES.MODE_CBC, iv)
        
        # Encrypt the padded data and encode the result as Base64
        encrypted_64 = base64.b64encode(cipher.encrypt(pad(data))).decode('ascii')
        
        # Encode the IV as Base64
        iv_64 = base64.b64encode(iv).decode('ascii')
        
        # Create a JSON object containing the IV and encrypted data
        json_data = {'iv': iv_64, 'data': encrypted_64}
        
        # Encode the JSON object as a Base64 string
        clean = base64.b64encode(json.dumps(json_data).encode('ascii'))
    except Exception as e:
        print("Cannot encrypt data...")
        print(e)
        exit(1)
    return clean

def my_decrypt(data, passphrase):
    """
    Decrypt data using AES-256-CBC with a provided IV.
    
    Args:
        data (str): The Base64-encoded JSON string containing the IV and encrypted data.
        passphrase (str): The passphrase in hex format, generated with 'openssl rand -hex 32'.
        
    Returns:
        str: The decrypted plaintext data.
    """
    try:
        # Unpadding function to remove padding added during encryption
        unpad = lambda s: s[:-s[-1]]
        
        # Convert the passphrase from hex to bytes
        key = binascii.unhexlify(passphrase)
        
        # Decode the Base64-encoded JSON string and parse it
        encrypted = json.loads(base64.b64decode(data).decode('ascii'))
        
        # Extract the encrypted data and IV from the JSON object
        encrypted_data = base64.b64decode(encrypted['data'])
        iv = base64.b64decode(encrypted['iv'])
        
        # Initialize the AES cipher in CBC mode with the extracted IV
        cipher = AES.new(key, AES.MODE_CBC, iv)
        
        # Decrypt the encrypted data and remove padding
        decrypted = cipher.decrypt(encrypted_data)
        clean = unpad(decrypted).decode('ascii').rstrip()
    except Exception as e:
        print("Cannot decrypt data...")
        print(e)
        exit(1)
    return clean
