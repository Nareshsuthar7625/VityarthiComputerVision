import os
import cv2

class PostureDetector:
    def __init__(self):
        xml_path = os.path.join(os.path.dirname(__file__), 'haarcascade_frontalface_default.xml')
        self.face_cascade = cv2.CascadeClassifier(xml_path)
        
        if self.face_cascade.empty():
            raise RuntimeError(f"Failed to load cascade from {xml_path}")
            
        self.initial_y = None
        self.calibration_frames = 0
        self.calibrated = False

    def track(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # equalize lighting to make detection robust in dimmer rooms
        gray = cv2.equalizeHist(gray)

        # lowered minNeighbors from 5 to 4 and scaleFactor to 1.1 for easier face locking
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(60, 60))

        if len(faces) == 0:
            return None, False

        # Pick largest face
        x, y, w, h = sorted(faces, key=lambda f: f[2] * f[3], reverse=True)[0]

        # Average the first 15 frames for a solid sitting baseline
        if not self.calibrated:
            if self.initial_y is None:
                self.initial_y = y
            else:
                self.initial_y = (self.initial_y + y) / 2
            self.calibration_frames += 1
            if self.calibration_frames >= 15:
                self.calibrated = True

        # Lowered slouch trigger: head drops down by more than 20 pixels
        is_slouching = self.calibrated and (y - self.initial_y) > 20
        return (x, y, w, h), is_slouching

    def release(self):
        pass