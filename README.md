# Real-Time Ergonomic Posture & Fatigue Monitor

A simple desktop script that monitors your sitting posture and flags eye drowsiness in real time using a standard webcam.

Instead of burning CPU cycles with deep-learning networks, it relies on OpenCV Haar cascades to detect face drop and eye closure fast on normal hardware.

---

## Overview

Sitting at a desk for long stretches almost always causes slouching, neck craning, and dry eyes.

This project captures video straight from your webcam, tracks your head position, and checks if you drop too far down from where you started sitting. It also crops the eye region to check if you keep your eyes closed for too long. Whenever slouching or drowsiness continues for half a second, warning banners pop up on screen so you can fix your posture right away.

---

## Features

- **Quick Startup Calibration**: The script takes the average vertical position of your face during the first 15 frames to lock in your normal sitting height. You do not have to mess with manual calibration settings.
- **Slouch Flagging**: If your face moves downward past 20 pixels from that starting baseline, it gets flagged as a slouch.
- **Eye Closure Checks**: Cuts the face box down to the top 60% area so the cascade focuses purely on your eyes and ignores your nose or mouth.
- **Debounce Filter**: Quick head shifts or natural blinks won't set off alarms. It requires 12 continuous frames (~0.5s) of an issue before showing alerts.
- **Live Visual HUD**: Draws clean bounding boxes and status notifications directly on the mirrored camera feed.
- **Session Telemetry**: Appends tracking status, visible eye counts, and warning flags into `session_log.csv` with timestamps whenever the script runs.

---

## Tech Stack & Dependencies

- **Language**: Python 3.9+
- **Core Library**: OpenCV (`opencv-python`)
- **Model Files**:
  - `haarcascade_frontalface_default.xml` (inside `src/`)
  - `haarcascade_eye.xml` (inside `src/`)
- **Hardware**: Any basic USB or laptop webcam (640x480)

---

## Setup & Running the Project

### 1. Clone the repo
git clone https://github.com/Nareshsuthar7625/VityarthiComputerVision.git
cd VityarthiComputerVision

### 2. Set up virtual environment
Windows:
python -m venv venv
venv\Scripts\activate

macOS / Linux:
python3 -m venv venv
source venv/bin/activate

### 3. Install packages
pip install opencv-python

*(Confirm both Haar cascade XML files are placed inside the `src/` directory).*

### 4. Run the monitor
Sit up straight facing the camera, then run:
python main.py

*Note: The script establishes your posture baseline during the first 15 frames, so make sure you sit in a natural upright position right as it starts up.*

To close the window and exit, press the `q` key on your keyboard.

---

## Testing & Verification

### Running Unit Tests
To run the automated tests:
python -m unittest discover tests

### Manual Checks
1. **Calibration**: Run `python main.py` and verify the HUD shows `User Tracked` in green after a second.
2. **Posture Warning**: Slouch down in your chair until your head drops noticeably. The box should switch red and trigger `POSTURE ALERT: Sit up straight!` after ~12 frames.
3. **Drowsiness Warning**: Hold your head still and keep your eyes shut. The system should display `DROWSINESS ALERT: Keep eyes open!` within half a second.
4. **Log Inspection**: Hit `q` to exit, then open `session_log.csv` to confirm the rows recorded your test states with valid timestamps.
