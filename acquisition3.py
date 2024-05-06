import cv2
import dlib
import numpy as np

# Frame Capturing
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 30)  # Set frame rate to 30 FPS

eye_landmarks = []
head_landmarks = []

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Facial Detection
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detector = dlib.get_frontal_face_detector()
    faces = detector(gray_frame)

    if len(faces) > 0:
        # Select the face with the largest bounding box (closest to the camera)
        face = max(faces, key=lambda rect: rect.width() * rect.height())
        
        # Landmark Extraction
        predictor = dlib.shape_predictor(r"C:\Users\oazougagh\Desktop\Test\acquisition.py\shape_predictor_68_face_landmarks.dat")
        landmarks = predictor(gray_frame, face)

        # Extract relevant landmarks for eyes (points 36 to 47) and head orientation (points 30, 8, 36, 45, 48, 54)
        eye_landmarks = landmarks.parts()[36:48]
        head_landmarks = [landmarks.part(i) for i in [30, 8, 36, 45, 48, 54]]

        # Output example
        print("Eye Landmarks:", eye_landmarks)
        print("Head Landmarks:", head_landmarks)

    # Display the frame with landmarks (for visualization purposes)
    for point in eye_landmarks + head_landmarks:
        cv2.circle(frame, (point.x, point.y), 2, (0, 255, 0), -1)

    cv2.imshow('Frame with Landmarks', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
