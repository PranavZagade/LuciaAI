# Face Recognition System using OpenCV
# This script performs the following tasks:
# 1. Loads images from a directory, converts them to grayscale, and assigns labels.
# 2. Trains an LBPH face recognizer using the labeled images.
# 3. Captures real-time video feed, detects faces, and identifies matches.
# 4. Displays the confidence level for matches and marks unknown faces.

import cv2
import os
import numpy as np

# Function to load images from a directory and assign labels
def get_images_and_labels(path):
    # Get all image file paths with supported extensions
    image_paths = [os.path.join(path, f) for f in os.listdir(path) if f.endswith(('.png', '.jpg', '.jpeg'))]
    images = []  # List to store grayscale images
    labels = []  # List to store corresponding labels
    label = 0  # Start with label 0

    for image_path in image_paths:
        # Read the image from the file
        image = cv2.imread(image_path)
        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Add the grayscale image and its label to the lists
        images.append(gray)
        labels.append(label)
        label += 1  # Increment label for the next image

    return images, labels

# Path to the directory containing images for training
images_path = 'images'

# Load training images and their labels
images, labels = get_images_and_labels(images_path)

# Create an LBPH face recognizer (Local Binary Patterns Histogram)
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Train the face recognizer using the images and labels
recognizer.train(images, np.array(labels))

# Initialize the webcam for live video capture
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    print("Camera is active. Press 'q' to quit.")

    while True:
        # Capture a frame from the webcam
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame. Exiting...")
            break

        # Convert the frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Load the pre-trained Haar Cascade for face detection
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # Detect faces in the grayscale frame
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            # Extract the region of interest (ROI) corresponding to the face
            roi_gray = gray[y:y+h, x:x+w]

            # Predict the label and confidence for the detected face
            label, confidence = recognizer.predict(roi_gray)

            # Normalize confidence to a similarity percentage (higher is better)
            similarity = max(0, 100 - confidence)  # Confidence lower means better match

            if confidence < 100:  # Threshold for recognizing faces
                # Display match percentage for recognized faces
                text = f"Match: {similarity:.2f}%"
                cv2.putText(frame, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
            else:
                # Label face as "Unknown" if not confidently recognized
                cv2.putText(frame, "Unknown", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

            # Draw a rectangle around the detected face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Show the processed video frame
        cv2.imshow('Face Recognizer', frame)

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()
