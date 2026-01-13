import threading
from ai_modules.control import stop_event
from ai_modules.video_proctor import start_video_proctor
from ai_modules.audio_monitor import monitor_audio

def start_proctoring():
    stop_event.clear()

    threading.Thread(target=start_video_proctor, daemon=True).start()
    threading.Thread(target=monitor_audio, daemon=True).start()
