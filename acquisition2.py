import cv2
import dlib
import numpy as np
import time, os, glob, threading
from imutils import face_utils




class Acquisition(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.running = True

        #Initializing the camera and taking the instance
        self.camera = cv2.VideoCapture(0)
        self.camera.set(cv2.CAP_PROP_FPS, 40)

        #Initializing the face detector and landmark detector
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor(r"C:\Users\oazougagh\Desktop\Test\acquisition.py\shape_predictor_68_face_landmarks.dat")
        self.eye_landmarks = {'left'  : [], 'right' : []}

        (self.start_l, self.end_l) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
        (self.start_r, self.end_r) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

        # nose, chin, l_eye, r_eye, l_mouth, r_mouth
        self.index_orientation_landmarks = [30, 8, 36, 45, 48, 54]

        self.start_time = time.time()
        self.counter = 0    
        self.buffer = []
        self.accesible = False
        self.safe = False

        self.old_frames = {}
        self.frames = {}
        self.frame_indx_len = 0
        self.frame = None
    
    def run(self):
        print("[INFO] Acquisition Thread Opened")


while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = hog_face_detector(gray)
    print("Number of faces detected:", len(faces))
    
    for face in faces:

        face_landmarks = dlib_facelandmark(gray, face)

        for n in range(0, 16):
            x = face_landmarks.part(n).x
            y = face_landmarks.part(n).y
            cv2.circle(frame, (x, y), 1, (0, 255, 255), 1)
                

    cv2.imshow("Face Landmarks", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()