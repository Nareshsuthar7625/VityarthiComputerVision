import os
import cv2

class EyeDetector:
    def __init__(self):
        xml_path = os.path.join(os.path.dirname(__file__), 'haarcascade_eye.xml')
        self.eye_cascade = cv2.CascadeClassifier(xml_path)
        
        if self.eye_cascade.empty():
            raise RuntimeError(f"Failed to load cascade from {xml_path}")

    def track(self, frame, face_box):
        if face_box is None:
            return False, 0

        x, y, w, h = face_box
        roi_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)[y:y + int(h * 0.6), x:x + w]

        eyes = self.eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=4, minSize=(20, 20))
        num_eyes = len(eyes)

        eyes_closed = (num_eyes == 0)
        return eyes_closed, num_eyes

    def release(self):
        pass