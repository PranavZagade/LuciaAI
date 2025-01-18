'''
CODE DESCRIPTION:
This Python script uses OpenCV to capture real-time video from the default webcam and
display the video feed in a window. The video frames are captured in a loop and
displayed on the screen. The user can exit the program by pressing the 'q' key.
The program releases the webcam and closes any OpenCV windows when the loop ends.

Conclusion: This test will assist us in developing facial recognition technology.

'''
import cv2

# Initialize the video capture object with device index '0', which refers to the default webcam
cap = cv2.VideoCapture(0)

# Infinite loop to continuously capture frames from the webcam
while(True):
    # Capture frame-by-frame
    # 'ret' is a boolean indicating if the frame was successfully captured
    # 'frame' is the actual frame/image captured from the webcam
    ret, frame = cap.read()

    # Display the resulting frame in a window named 'frame'
    # Each captured frame is displayed in real-time
    cv2.imshow('frame', frame)

    # Check if the 'q' key is pressed to break the loop and stop video capture
    # cv2.waitKey(20) waits for 20 milliseconds to check for any keypress
    # '& 0xFF' is used to handle the keypress correctly across different systems
    # ord('q') gives the ASCII value of the letter 'q'
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break  # Exit the loop if the 'q' key is pressed

# When everything is done, release the capture object (free up the webcam for other applications)
cap.release()

# Close all OpenCV windows opened during the execution of the program
cv2.destroyAllWindows()
