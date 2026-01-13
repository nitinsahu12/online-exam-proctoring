import cv2
import time
import os
import mediapipe as mp
from ai_modules.control import stop_event

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

CAPTURE_DIR = "static/captures"
os.makedirs(CAPTURE_DIR, exist_ok=True)

LEFT_EYE = 33
RIGHT_EYE = 362

def start_video_proctor():
    cap = cv2.VideoCapture(0)
    last_capture = 0
    look_away_start = None

    while not stop_event.is_set():
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        mesh = face_mesh.process(rgb)

        status = "Normal"

        # ---- Face violations ----
        if len(faces) == 0:
            status = "No Face Detected"
        elif len(faces) > 1:
            status = "Multiple Faces Detected"

        # ---- Eye gaze ----
        if mesh.multi_face_landmarks:
            lm = mesh.multi_face_landmarks[0].landmark
            if lm[LEFT_EYE].x < 0.3 or lm[RIGHT_EYE].x > 0.7:
                if look_away_start is None:
                    look_away_start = time.time()
                elif time.time() - look_away_start > 3:
                    status = "Looking Away"
            else:
                look_away_start = None

        # ---- Save screenshot ----
        if status != "Normal" and time.time() - last_capture > 5:
            cv2.imwrite(f"{CAPTURE_DIR}/violation_{int(time.time())}.jpg", frame)
            last_capture = time.time()

        # ---- Draw ----
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

        cv2.putText(frame, status, (20,40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

        cv2.imshow("Exam Proctoring", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            stop_event.set()
            break

    cap.release()
    cv2.destroyAllWindows()
