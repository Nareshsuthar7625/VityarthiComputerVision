# Problem Statement & Project Scope

## Problem Statement
When studying or writing code at my desk for hours, I tend to unconsciously slouch downward and stare blankly at my monitor. This habit causes neck pain, rounded shoulders, and severe eye strain. Most students and desk workers do not realize they have bad posture until their back starts aching, and standard interval timers are annoying because they interrupt you even when you are sitting completely fine.

## Scope of the Project
This project provides a local, real-time Computer Vision application that uses an ordinary laptop webcam to monitor sitting posture and facial fatigue indicators. It establishes a sitting height baseline during the first couple seconds, continuously tracks face and eye coordinates, and flags visible on-screen warnings only when slouching or eye closure persists beyond a debounced threshold. It also records telemetry into a local CSV file for personal review.

## Target Users
- Students attending online courses or doing long assignments.
- Programmers and office workers bound to desks.
- Anyone wanting an ergonomic posture checker without wearing uncomfortable straps or sensor gadgets.

## High-Level Features
- Real-time frontal face tracking using OpenCV Haar cascades with histogram equalization for dim lighting.
- Region of Interest (ROI) slicing across the upper facial area for eye state tracking.
- Dynamic baseline calibration averaging the user's initial sitting height.
- Consecutive frame debounce logic to eliminate flickering alerts caused by quick normal head movements.
- Live on-screen Heads-Up Display (HUD) and timestamped CSV session logging.
