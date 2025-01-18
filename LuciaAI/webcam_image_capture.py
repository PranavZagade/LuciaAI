'''
CODE DESCRIPTION:
This script captures an image from the webcam after warming up the camera,
and saves it in the ImageTest folder. If the folder doesn’t exist,
the script creates it.

'''
import cv2
import os

# Set the camera port (0 is usually the default webcam, use 1 for an external webcam)
camera_port = 0

# Number of frames to capture for warming up the camera
ramp_frames = 10

# Initialize video capture using the specified camera port
# (0 refers to the default camera)
camera = cv2.VideoCapture(camera_port)

# Define a function to capture a frame (image) from the webcam
def get_image():
    retval, img = camera.read()  # captures frame from the webcam
    return img

# Warm-up phase: Capture and discard several frames to allow the camera to adjust (improves image quality)
for i in range(ramp_frames):
    temp = get_image()  # Capture a temporary image (not saved)
    print("CAPTURING PIC")  # Print a message indicating the frame is captured

# After the warm-up, capture the final image to be saved
camera_capture = get_image()

# Specify the directory where the image will be saved
output_dir = "ImageTest"  # Folder named 'ImageTest' will be used for saving the image

# Check if the folder exists, and if it doesn't, create it
if not os.path.exists(output_dir):
    os.makedirs(output_dir)  # Create the folder if it doesn't exist

# Define the path and filename where the image will be saved
file = os.path.join(output_dir, "test_image_f1.png")

# Save the captured image as 'test_image_f1.png' in the 'ImageTest' folder
cv2.imwrite(file, camera_capture)

# Release the camera resource so that it can be used by other applications
del camera

# Print a message to indicate the image has been saved successfully
print(f"Image saved to {file}")
