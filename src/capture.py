import cv2

class VideoCaptureHandler:
    def __init__(self, cam_id=0, w=640, h=480):
        self.cam_id = cam_id
        self.w = w
        self.h = h
        self.cap = None

    def start(self):
        self.cap = cv2.VideoCapture(self.cam_id)
        if not self.cap.isOpened():
            # fallback in case default index is occupied
            self.cap = cv2.VideoCapture(1)
            if not self.cap.isOpened():
                raise SystemExit("Error: Could not open any webcam.")
        
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.w)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.h)

    def read_frame(self):
        if not self.cap or not self.cap.isOpened():
            return False, None
        ret, frame = self.cap.read()
        if ret:
            # mirror frame horizontally so movements match user perspective
            frame = cv2.flip(frame, 1)
        return ret, frame

    def stop(self):
        if self.cap and self.cap.isOpened():
            self.cap.release()