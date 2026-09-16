import cv2
import config
from src.capture import VideoCaptureHandler
from src.posture_detector import PostureDetector
from src.eye_detector import EyeDetector
from src.alert_manager import AlertManager
from src.logger import SessionLogger

def run():
    cam = VideoCaptureHandler(config.CAM_ID, config.FRAME_W, config.FRAME_H)
    posture = PostureDetector()
    eyes = EyeDetector()
    hud = AlertManager()
    logger = SessionLogger(config.LOG_PATH)

    cam.start()

    slouch_cnt = 0
    fatigue_cnt = 0

    try:
        while True:
            ret, frame = cam.read_frame()
            if not ret:
                break

            # Module 1: Posture Tracking
            face_box, is_slouching = posture.track(frame)
            if is_slouching:
                slouch_cnt += 1
            else:
                slouch_cnt = max(0, slouch_cnt - 1)

            # Module 2: Eye Fatigue Tracking
            eyes_closed, num_eyes = eyes.track(frame, face_box)
            if face_box is not None and eyes_closed:
                fatigue_cnt += 1
            else:
                fatigue_cnt = max(0, fatigue_cnt - 1)

            slouch_warn = (slouch_cnt >= config.POSTURE_FAIL_LIMIT)
            fatigue_warn = (fatigue_cnt >= config.FATIGUE_FAIL_LIMIT)

            # Module 3: Render HUD & Log
            frame = hud.draw_hud(frame, face_box, num_eyes, slouch_warn, fatigue_warn)
            logger.record(face_box is not None, num_eyes, slouch_warn, fatigue_warn)

            cv2.imshow("Ergonomic Monitor - Press 'q' to Quit", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        cam.stop()
        posture.release()
        eyes.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    run()