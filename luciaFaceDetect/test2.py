# Real-Time Face Recognition for Access Control
# This script captures video from the webcam, detects a face, and predicts if the detected face matches the trained user.
# If confidence is above a threshold (85%), access is granted ("Unlocked"), otherwise access remains "Locked".
# The script uses a pre-trained model for prediction and a Haar Cascade for face detection.

import cv2
import numpy as np

# Import the pre-trained model for face recognition
from trainModel import model

# Load the Haar Cascade for face detection
face_classifier = cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')

# Function to detect face and extract the region of interest (ROI)
def face_detector(img, size=0.5):
    # Convert the image to grayscale for face detection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect faces in the image
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    if faces is ():  # If no face is detected, return the original image and an empty list
        return img, []

    for (x, y, w, h) in faces:
        # Draw a rectangle around the detected face
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        # Extract the face region and resize it to 200x200
        roi = img[y:y + h, x:x + w]
        roi = cv2.resize(roi, (200, 200))
    return img, roi  # Return the processed image and the cropped face region

# Initialize the webcam
cap = cv2.VideoCapture(0)
counter = 0  # Counter to track successful detections

# Start the video capture and processing loop
while True:
    ret, frame = cap.read()  # Capture a frame from the webcam
    image, face = face_detector(frame)  # Detect and extract the face

    try:
        # Convert the cropped face to grayscale for the prediction model
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

        # Predict the label and confidence for the detected face
        results = model.predict(face)

        # Calculate confidence as a percentage
        if results[1] < 500:  # Ensure confidence is within a valid range
            confidence = int(100 * (1 - (results[1]) / 400))
            display_string = str(confidence) + '% Confident it is User'

        # If confidence is high, grant access
        if confidence > 85:
            cv2.putText(image, "Unlocked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow('Face Recognition', image)
            counter += 1  # Increment the counter for consecutive successful detections
            print(counter)

            if counter > 100:  # If user is recognized for 100 frames, consider them logged in
                print("You are logged in")
                break

        else:
            # If confidence is low, deny access
            cv2.putText(image, "Locked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow('Face Recognition', image)

    except:
        # Handle cases where no face is found in the frame
        cv2.putText(image, "No Face Found", (220, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
        cv2.putText(image, "Locked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow('Face Recognition', image)
        pass

    # Exit the loop when the Enter key (ASCII 13) is pressed
    if cv2.waitKey(1) == 13:
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
