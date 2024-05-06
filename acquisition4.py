import cv2
import face_detection
from dlib import get_landmarks
import numpy as np

# Initialize the camera
camera = cv2.VideoCapture(0)

# Initialize the face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    # Capture a frame from the camera
    ret, frame = camera.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Extract facial landmarks from each detected face
    for (x, y, w, h) in faces:
        face_image = frame[y:y+h, x:x+w]
        face_landmarks = face_detection.getLandmarks(face_image)

        # Do something with the facial landmarks (e.g. draw them on the frame)
        for landmark in face_landmarks.parts():
            cv2.circle(frame, (landmark.x, landmark.y), 2, (0, 255, 0), -1)

    # Display the frame
    cv2.imshow('Face Detection', frame)

    # Exit if the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and destroy all windows
camera.release()
cv2.destroyAllWindows()