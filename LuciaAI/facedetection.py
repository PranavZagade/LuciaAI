'''
 CODE DESCRIPTION:
This Python script uses OpenCV to detect faces in real-time from the webcam feed.
It applies a Haar Cascade classifier to detect faces, draws rectangles around them,
and displays the result. The program runs until the user presses 'q' to exit.
'''

import cv2

# Load Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt2.xml')

# Function to detect faces and draw a rectangle around them
def face_extractor(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) == 0:
        return None

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    return img

# Start capturing video from webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if face_extractor(frame) is not None:
        cv2.imshow('Face Detection', frame)
    else:
        print("Face not found")

    # Break loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam and close windows
cap.release()
cv2.destroyAllWindows()
