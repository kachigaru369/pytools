import socket

target = input("enter ur doamin:")
ports = [21,22,23,25,53,80,110,139,143,443,445,8080]

try:
    socket.setdefaulttimeout(1)
    ip = socket.gethostbyname(target)
    for port in ports:
        sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        # sock.settimeout(1)
        result = sock.connect_ex((ip, port))

        if result == 0:
            print(f"port {port} is OPEN")
        else:
            print(f"port {port} is CLOSED")

        sock.close()
except:
    print("can not reach the doamin")

# socket.setdefaulttimeout(1)
# socket.socket(socket.AF_INET , socket.SOCK_STREAM)
# sock.connect_ex((ip, port))








# import socket

# target = input("Enter domain or IP: ")
# ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 8080]

# try:
#     ip = socket.gethostbyname(target)
#     print(f"\nScanning target: {ip}\n")
    
#     for port in ports:
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         sock.settimeout(1)
#         result = sock.connect_ex((ip, port))

#         if result == 0:
#             print(f"[+] Port {port} is OPEN")
#         else:
#             print(f"[-] Port {port} is CLOSED")

#         sock.close()

# except socket.gaierror:
#     print("[-] Invalid domain or cannot resolve host.")
# except Exception as e:
#     print(f"[-] Unexpected error: {e}")
