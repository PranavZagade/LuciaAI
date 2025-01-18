# Hiding Text in an Image Using LSB Encoding
# This script hides a secret text message in an image by modifying the least significant bits (LSBs)
# of the RGB pixel values. The modified image is saved as a new file with the encoded message.

from PIL import Image

# Function to convert a message to binary
def message_to_binary(message):
    """
    Converts a string message into its binary representation.
    
    Args:
        message (str): The text message to convert.
        
    Returns:
        str: A binary string representing the message.
    """
    return ''.join(format(ord(char), '08b') for char in message)

# Hide text in an image using LSB encoding
def hide_text_in_image(input_image_path, output_image_path, secret_message):
    """
    Hides a secret text message in an image by modifying the least significant bits of the pixel values.
    
    Args:
        input_image_path (str): Path to the input image.
        output_image_path (str): Path to save the output image with the hidden message.
        secret_message (str): The message to hide in the image.
        
    Prints:
        str: Confirmation message when the process is complete.
    """
    # Load the image
    image = Image.open(input_image_path)
    # Convert the message to binary and add a delimiter to mark the end of the message
    binary_message = message_to_binary(secret_message) + '1111111111111110'  # End of message delimiter
    binary_index = 0  # Tracks the position in the binary message

    # Convert the image to RGB mode if it isn't already
    image = image.convert("RGB")
    # Get the pixel data as a list
    pixels = list(image.getdata())

    # Create a list to hold the modified pixels
    new_pixels = []
    for pixel in pixels:
        r, g, b = pixel  # Get the red, green, and blue values of the pixel

        # Modify the LSBs of the red, green, and blue channels to store the binary message
        if binary_index < len(binary_message):
            r = (r & ~1) | int(binary_message[binary_index])  # Modify the LSB of the red channel
            binary_index += 1
        if binary_index < len(binary_message):
            g = (g & ~1) | int(binary_message[binary_index])  # Modify the LSB of the green channel
            binary_index += 1
        if binary_index < len(binary_message):
            b = (b & ~1) | int(binary_message[binary_index])  # Modify the LSB of the blue channel
            binary_index += 1

        # Append the modified pixel to the new pixel list
        new_pixels.append((r, g, b))

    # Create a new image using the modified pixel data
    image.putdata(new_pixels)
    # Save the new image to the specified output path
    image.save(output_image_path)
    print(f"Text hidden in image and saved as {output_image_path}")

# Example usage
hide_text_in_image('stegano.png', 'encoded_image.png', 'I am Test Hidden Message')
