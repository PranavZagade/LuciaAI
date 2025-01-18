# Webcam Face Detection and Image Saving Script
# This script captures live video from the webcam, detects faces using a pre-trained Haar Cascade model, 
# and allows saving images either automatically every 5 seconds or manually by pressing the 's' key. 
# The captured images are saved in the 'images' directory.

import cv2
import os
import time

# Directory where the captured images will be saved
save_path = 'images'
os.makedirs(save_path, exist_ok=True)  # Create the directory if it doesn't exist

# Load the Haar Cascade model for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is successfully opened
if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    print("Camera is active. Press 's' to save an image manually, 'q' to quit.")
    img_counter = 0  # Counter for naming saved images
    start_time = time.time()  # Timer for automatic saving

    while True:
        # Capture the current frame from the webcam
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame. Exiting...")
            break

        # Convert the frame to grayscale (required for face detection)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale frame
        faces = face_cascade.detectMultiScale(
            gray, 
            scaleFactor=1.1, 
            minNeighbors=5, 
            minSize=(30, 30)
        )

        # Draw green rectangles around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the live video feed with rectangles
        cv2.imshow('Webcam Live with Face Detection', frame)

        # Save an image automatically every 5 seconds
        if time.time() - start_time > 5:
            img_name = f"{save_path}/img_{img_counter:04d}.png"  # Generate image file name
            cv2.imwrite(img_name, frame)  # Save the current frame
            print(f"{img_name} written!")  # Confirm image save
            img_counter += 1  # Increment the counter for the next image
            start_time = time.time()  # Reset the timer

        # Save an image manually when 's' is pressed
        if cv2.waitKey(1) & 0xFF == ord('s'):
            img_name = f"{save_path}/img_{img_counter:04d}.png"  # Generate image file name
            cv2.imwrite(img_name, frame)  # Save the current frame
            print(f"{img_name} written!")  # Confirm image save
            img_counter += 1  # Increment the counter for the next image

        # Exit the program when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Exiting...")
            break

    # Release the webcam and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()
