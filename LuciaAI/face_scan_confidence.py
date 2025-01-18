'''
CODE DESCRIPTION:
This script is used for real-time face recognition using a webcam. Before running this code,
you need to collect face samples using face_sample_collector.py and train a face recognition model
using trainModel.py. Once the model is trained, this script can use the webcam to detect and recognize faces,
displaying whether the user is recognized ("Unlocked") or not ("Locked"). The process continues until the Enter key
is pressed or the user is recognized in 100 frames.

'''
import cv2
from trainModel import model  # Import the pre-trained model from trainModel.py

# Load the Haar Cascade classifier for face detection
face_classifier = cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')

# Function to detect the face in the image
def face_detector(img, size=0.5):
    # Convert the image to grayscale (face detection works better on grayscale images)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Detect faces using the Haar Cascade classifier
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    # If no face is found, return the original image and an empty list
    if len(faces) == 0:
        return img, []

    # For each face found, draw a rectangle and extract the face region (ROI)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)  # Draw rectangle around face
        roi = img[y:y + h, x:x + w]  # Extract the face region (ROI)
        roi = cv2.resize(roi, (200, 200))  # Resize the face for model input
    return img, roi  # Return the image with rectangle and the face region (ROI)

# Open the webcam for real-time face recognition
cap = cv2.VideoCapture(0)  # Use the default webcam
counter = 0  # Initialize a counter to count recognized frames

# Start real-time face recognition
while True:
    ret, frame = cap.read()  # Capture each frame from the webcam
    image, face = face_detector(frame)  # Detect the face in the current frame

    try:
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)  # Convert the detected face to grayscale

        # Use the pre-trained model to predict the face
        results = model.predict(face)  # Get prediction and confidence value

        if results[1] < 500:  # Lower confidence value indicates a better match
            confidence = int(100 * (1 - (results[1]) / 400))  # Calculate confidence percentage
            display_string = str(confidence) + '% Confident it is User'

        # If confidence is higher than 85%, unlock and increment counter
        if confidence > 85:
            cv2.putText(image, "Unlocked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow('Face Recognition', image)
            counter += 1  # Increment counter for each recognized frame
            print(counter)  # Print the counter to the console
            
            if counter > 100:  # If user is recognized in 100 frames, consider logged in
                print("You are logged in")
                break

        # If confidence is below 85%, show "Locked"
        else:
            cv2.putText(image, "Locked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow('Face Recognition', image)

    # If no face is detected, show "No Face Found" and "Locked"
    except:
        cv2.putText(image, "No Face Found", (220, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
        cv2.putText(image, "Locked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow('Face Recognition', image)
        pass

    # Exit the loop if the Enter key is pressed
    if cv2.waitKey(1) == 13:  # 13 is the ASCII code for the Enter key
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
