# Face Emotion Analysis Using DeepFace
# This script reads an image, displays it using Matplotlib, and analyzes the emotion in the face using DeepFace.

# Import the required modules
import cv2  # OpenCV for image processing
import matplotlib.pyplot as plt  # For displaying the image
from deepface import DeepFace  # DeepFace library for emotion analysis

# Step 1: Read the image
img = cv2.imread('image1.jpg')  # Replace 'image1.jpg' with the path to your image

# Step 2: Display the image using Matplotlib
plt.imshow(img[:, :, ::-1])  # Convert BGR to RGB format for correct color rendering
plt.show()  # Display the image

# Step 3: Analyze the emotion in the image
result = DeepFace.analyze(img, actions=['emotion'])  # Analyze emotions in the image

# Step 4: Print the result of the analysis
print(result)  # Print the analysis result, including detected emotions
