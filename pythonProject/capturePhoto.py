# Capturing Images from Webcam Using OpenCV
# This script captures 10 images from the webcam and saves them as sequentially named PNG files.

import cv2  # Import the OpenCV library

# Initialize the webcam (camera index 0 for the default webcam)
camera = cv2.VideoCapture(0)

# Loop to capture and save 10 images
for i in range(10):
    # Capture a single frame from the webcam
    return_value, image = camera.read()
    
    # Check if the frame was successfully captured
    if return_value:
        # Save the captured frame as a PNG image file
        cv2.imwrite('opencv' + str(i) + '.png', image)
    else:
        print(f"Failed to capture image {i}")

# Release the webcam resources
del(camera)
