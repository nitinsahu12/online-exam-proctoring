📘 AI-Based Online Exam Proctoring System

An advanced Python project that monitors online exams using computer vision and audio analysis.
The system detects suspicious behavior in real time and generates a proctoring report after the exam.

🚀 Features

Real-time face detection

Multiple face detection

Eye gaze / distraction detection

Audio monitoring for suspicious sounds

Screenshot capture for violations

Automated risk-based proctoring report

Clean shutdown using shared threading control

Web interface using Flask

🧠 How the System Works

User logs in and starts the exam

Webcam and microphone monitoring begin automatically

The system checks for:

Face absence or multiple faces

Looking away from the screen

Continuous background noise or speech

Violations are logged with screenshots

After the exam ends, a final report is generated

🏗️ Project Architecture

Flask handles routing and UI

OpenCV processes webcam frames

MediaPipe tracks facial landmarks and eye movement

SoundDevice monitors microphone input

A shared threading.Event ensures all modules stop safely together

👤 Author

Nitin Kumar
B.Tech (ECE)
Python | Computer Vision | Cloud | Full-Stack
