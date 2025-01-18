'''
CODE DESCRIPTION:
This script is designed to capture 100 face samples from the webcam, save them as grayscale images,
and display live feedback during the process. After collecting the samples, it shows a message
indicating that the face scan is complete.
'''
import cv2
import numpy as np

# Load HAAR face classifier
face_classifier = cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')


# Load functions
def face_extractor(img):
    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    # Check if no faces are found
    if len(faces) == 0:
        return None

    # Crop the face if detected
    for (x, y, w, h) in faces:
        cropped_face = img[y:y + h, x:x + w]

    return cropped_face


# Initialize Webcam
cap = cv2.VideoCapture(0)
count = 0

# Set the window size to a larger one
cv2.namedWindow("Face Cropper", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Face Cropper", 600, 400)

# Collect 100 samples of your face from webcam input
while True:
    ret, frame = cap.read()

    # Display "Scanning" message on the frame
    cv2.putText(frame, "Scanning...", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    if face_extractor(frame) is not None:
        count += 1
        face = cv2.resize(face_extractor(frame), (200, 200))
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

        # Save file in specified directory with unique name
        file_name_path = './Myfaces/user/' + str(count) + '.jpg'
        cv2.imwrite(file_name_path, face)

        # Put count on images and display live count
        cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('Face Cropper', face)

    else:
        print("Face not found")

    if cv2.waitKey(1) == 13 or count == 100:  # 13 is the Enter Key
        break

cap.release()
cv2.destroyAllWindows()

# Show "Face Scan Completed" after finishing the process
print("Face Scan Completed")
cv2.namedWindow("Face Scan Completed", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Face Scan Completed", 600, 400)
completed_frame = np.zeros((400, 600, 3), dtype=np.uint8)
cv2.putText(completed_frame, "Face Scan Completed", (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 4)
cv2.imshow("Face Scan Completed", completed_frame)
cv2.waitKey(3000)  # Wait for 3 seconds
cv2.destroyAllWindows()
