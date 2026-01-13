# AI-Based Online Exam Proctoring System

An advanced Python-based system that monitors online exams using computer vision and audio analysis.  
It detects suspicious behavior in real time and generates a proctoring report after the exam.

---

## Features

- Real-time face detection using webcam  
- Multiple-face detection  
- Eye gaze and distraction detection  
- Audio monitoring for suspicious sounds  
- Screenshot capture as violation evidence  
- Automated risk-based proctoring report  
- Clean multi-threaded shutdown using shared control  
- Web interface built with Flask  

---

## How the System Works

1. User logs in and starts the exam  
2. Webcam and microphone monitoring start automatically  
3. The system continuously checks for:
   - No face or multiple faces
   - Looking away from the screen
   - Continuous background noise or speech
4. Violations are logged with screenshots
5. After the exam ends, a final proctoring report is generated

---

## Project Architecture

- Flask handles routing and web pages  
- OpenCV processes live webcam frames  
- MediaPipe tracks facial landmarks and eye movement  
- SoundDevice monitors microphone input  
- A shared `threading.Event` ensures all modules stop safely together  

---

## Folder Structure
online-exam-proctoring/
│
├── app.py
├── requirements.txt
│
├── ai_modules/
│ ├── control.py
│ ├── video_proctor.py
│ ├── audio_monitor.py
│ └── violation_tracker.py
│
├── templates/
│ ├── login.html
│ ├── exam.html
│ └── report.html
│
├── static/
│ ├── css/
│ │ └── style.css
│ └── captures/
│
└── .gitignore


---

## Technologies Used

- Python 3.10  
- Flask  
- OpenCV  
- MediaPipe  
- NumPy  
- SoundDevice  
- HTML and CSS  

---

## Author

- Nitin Kumar
- B.Tech (ECE)  
- Python | C++ | Cloud | Full-Stack 

