import csv
import os
import time

class SessionLogger:
    def __init__(self, filepath="session_log.csv"):
        self.filepath = filepath
        if not os.path.exists(self.filepath):
            with open(self.filepath, mode='w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Timestamp", "Face_Detected", "Eyes_Count", "Slouch_Alert", "Fatigue_Alert"])

    def record(self, face_detected, eyes_count, slouch_alert, fatigue_alert):
        with open(self.filepath, mode='a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                time.strftime("%Y-%m-%d %H:%M:%S"),
                1 if face_detected else 0,
                eyes_count,
                1 if slouch_alert else 0,
                1 if fatigue_alert else 0
            ])