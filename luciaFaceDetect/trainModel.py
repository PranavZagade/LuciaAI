# Training Face Recognition Model Using LBPH (Local Binary Patterns Histograms)
# This script reads grayscale face images from a specified directory, assigns labels to each image, 
# and trains an LBPH-based face recognizer model. The trained model can then be used for face recognition.

import cv2
import numpy as np
from os import listdir
from os.path import isfile, join

# Path to the directory containing the face images
data_path = './faces/user/'
# List all files in the directory
onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]

# Create lists to store training data and their corresponding labels
Training_Data, Labels = [], []

# Loop through each file in the directory to process images
for i, files in enumerate(onlyfiles):
    # Construct the full path to the image file
    image_path = data_path + onlyfiles[i]
    # Read the image in grayscale mode
    images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # Add the image to the training data list
    Training_Data.append(np.asarray(images, dtype=np.uint8))
    # Use the file index as the label
    Labels.append(i)

# Convert the labels list into a numpy array
Labels = np.asarray(Labels, dtype=np.int32)

# Initialize the LBPH face recognizer
model = cv2.face.LBPHFaceRecognizer_create()

# NOTE: For OpenCV 3.x, use cv2.face.createLBPHFaceRecognizer()

# Train the face recognizer model using the training data and labels
model.train(np.asarray(Training_Data), np.asarray(Labels))
print("Model trained successfully")
