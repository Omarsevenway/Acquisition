import cv2
import time
import threading
from acquisition5 import Acquisition

def main():
    # Create the Acquisition thread
    acquisition_thread = Acquisition()
    acquisition_thread.start()

    # Wait for the user to press the 'q' key to exit
    while True:
        acquisition_thread.run()
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    # Stop the Acquisition thread
    acquisition_thread.running = False
    acquisition_thread.join()
    acquisition_thread.get_closesed_face()
    # Release the camera
    acquisition_thread.camera.release()

if __name__ == '__main__':
    main()
    