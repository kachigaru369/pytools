import socket

target = input("enter domain(e.g. google.com):")
hostname = socket.gethostname()
ip_system = socket.gethostbyname(hostname)
try:
    ip = socket.gethostbyname(target)
    print(f"[+] IP address is:{ip}")
    print(f"your system name: {hostname}")
    print(f"your ip address is:{ip_system}")
except:
    print("[-] failed to get ip address")


# socket.gethostname()
# socket.gethostbyname()