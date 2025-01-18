"""
This script captures video from the webcam and uses OpenCV's Haar Cascade Classifier
to detect faces in real-time. It draws rectangles around detected faces and displays
the video feed in a window.
"""

import cv2  # OpenCV library for computer vision tasks

# Load the pre-trained Haar Cascade Classifier for face detection
# Ensure the XML file 'haarcascade_frontalface_default.xml' is in the working directory
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Start capturing video from the webcam
cap = cv2.VideoCapture(0)  # Use 0 for the default camera
# Alternatively, you can use a video file by providing its path:
# cap = cv2.VideoCapture('filename.mp4')

while True:
    # Read a frame from the video feed
    _, img = cap.read()  # `_` captures the return value, `img` is the frame

    # Convert the frame to grayscale (required for face detection)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    # Parameters:
    # - gray: input image
    # - 1.1: scale factor for image resizing
    # - 4: minimum number of neighbors a rectangle needs to be retained
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        # (x, y) is the top-left corner, (w, h) are the width and height of the rectangle
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Blue rectangle, thickness=2

    # Display the frame with rectangles in a window named 'img'
    cv2.imshow('img', img)

    # Stop the loop if the Escape key (key code 27) is pressed
    k = cv2.waitKey(30) & 0xff  # Wait 30ms for a key press
    if k == 27:
        break

# Release the VideoCapture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
