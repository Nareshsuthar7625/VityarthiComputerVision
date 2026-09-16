import cv2

class AlertManager:
    def __init__(self):
        self.font = cv2.FONT_HERSHEY_SIMPLEX

    def draw_hud(self, frame, face_box, num_eyes, slouch_warn, fatigue_warn):
        h, w = frame.shape[:2]

        # Top status card
        cv2.rectangle(frame, (10, 10), (300, 80), (25, 25, 25), -1)

        if face_box is not None:
            x, y, fw, fh = face_box
            color = (0, 0, 255) if slouch_warn else (0, 255, 0)
            cv2.rectangle(frame, (x, y), (x + fw, y + fh), color, 2)
            cv2.putText(frame, "User Tracked", (20, 38), self.font, 0.55, (240, 240, 240), 1, cv2.LINE_AA)
            cv2.putText(frame, f"Eyes Tracked: {num_eyes}", (20, 65), self.font, 0.55, (240, 240, 240), 1, cv2.LINE_AA)
        else:
            cv2.putText(frame, "Looking for user...", (20, 48), self.font, 0.55, (0, 165, 255), 1, cv2.LINE_AA)

        # Warning banners
        if slouch_warn:
            cv2.rectangle(frame, (15, h - 90), (w - 15, h - 55), (0, 0, 220), -1)
            cv2.putText(frame, "POSTURE ALERT: Sit up straight!", (30, h - 68),
                        self.font, 0.65, (255, 255, 255), 2, cv2.LINE_AA)

        if fatigue_warn:
            cv2.rectangle(frame, (15, h - 50), (w - 15, h - 15), (0, 140, 255), -1)
            cv2.putText(frame, "DROWSINESS ALERT: Keep eyes open!", (30, h - 28),
                        self.font, 0.65, (255, 255, 255), 2, cv2.LINE_AA)

        return frame