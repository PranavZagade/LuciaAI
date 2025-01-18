# Hidden Text Retrieval from an Image Using Steganography
# This script extracts binary data encoded in the least significant bits (LSB) of an image's RGB pixel values
# and converts it back to a human-readable secret message. It assumes the message is terminated by a delimiter.

from PIL import Image

# Function to extract binary data from an image
def extract_binary_from_image(image_path):
    """
    Extracts binary data hidden in the least significant bits (LSB) of an image.
    
    Args:
        image_path (str): Path to the image containing the hidden data.
        
    Returns:
        str: Binary string representing the hidden message.
    """
    # Open the image file
    image = Image.open(image_path)
    # Ensure the image is in RGB format
    image = image.convert("RGB")
    # Get the pixel values as a list
    pixels = list(image.getdata())

    binary_message = ""  # Initialize a string to hold the binary message

    # Loop through each pixel in the image
    for pixel in pixels:
        r, g, b = pixel  # Extract RGB values of the pixel
        # Extract the least significant bit (LSB) from each channel
        binary_message += str(r & 1)
        binary_message += str(g & 1)
        binary_message += str(b & 1)

        # Check for the end-of-message delimiter '1111111111111110'
        if binary_message[-16:] == '1111111111111110':
            break

    # Return the binary message without the delimiter
    return binary_message[:-16]

# Function to convert binary string back to text
def binary_to_message(binary_message):
    """
    Converts a binary string to a text message.
    
    Args:
        binary_message (str): Binary string representing the hidden message.
        
    Returns:
        str: Decoded text message.
    """
    # Split the binary string into chunks of 8 bits and convert each to a character
    chars = [chr(int(binary_message[i:i + 8], 2)) for i in range(0, len(binary_message), 8)]
    return ''.join(chars)

# Function to retrieve the hidden text from an image
def retrieve_text_from_image(image_path):
    """
    Retrieves and decodes the hidden text message from an image.
    
    Args:
        image_path (str): Path to the image containing the hidden text.
        
    Prints:
        str: The retrieved secret message.
    """
    # Extract the binary message from the image
    binary_message = extract_binary_from_image(image_path)
    # Decode the binary message to text
    secret_message = binary_to_message(binary_message)
    # Display the retrieved message
    print(f"Retrieved secret message: {secret_message}")

# Example usage
retrieve_text_from_image('encoded_image.png')
