# Face Sample Collection Script
# This script uses a webcam to capture 100 face samples, processes them by detecting and cropping the face region,
# and saves the grayscale cropped faces into a specified directory. It uses a pre-trained Haar Cascade classifier
# for face detection and displays the live feed with a counter.

import cv2
import numpy as np

# Load the pre-trained Haar Cascade model for face detection
face_classifier = cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')

# Function to detect faces and extract the cropped face region
def face_extractor(img):
    # Convert the image to grayscale for face detection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect faces in the image
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    # If no faces are detected, return None
    if faces == ():
        return None

    # Crop the first detected face (assumes one face per frame)
    for (x, y, w, h) in faces:
        cropped_face = img[y:y + h, x:x + w]

    return cropped_face

# Initialize the webcam for capturing video
cap = cv2.VideoCapture(0)
count = 0  # Counter for the number of face samples collected

# Start capturing and processing frames
while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Check if a face is detected in the frame
    if face_extractor(frame) is not None:
        count += 1  # Increment the sample counter
        # Resize the cropped face to a fixed size (200x200)
        face = cv2.resize(face_extractor(frame), (200, 200))
        # Convert the cropped face to grayscale
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

        # Define the file path and save the grayscale face image
        file_name_path = './faces/user/' + str(count) + '.jpg'
        cv2.imwrite(file_name_path, face)

        # Display the sample count on the frame
        cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        # Show the cropped face in a separate window
        cv2.imshow('Face Cropper', face)

    else:
        print("Face not found")  # Notify if no face is detected
        pass

    # Break the loop if 'Enter' key is pressed or 100 samples are collected
    if cv2.waitKey(1) == 13 or count == 100:  # 13 is the ASCII code for Enter key
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
print("Collecting Samples Complete")
