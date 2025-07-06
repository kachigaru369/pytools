import requests

url = input("enter url:")

try:
    response = requests.get(url)
    print("status code:", response.status_code)

    if response.status_code == 200:
        print("[+] website is up")
    else:
        print("[-] website is down", response.status_code)

except:
    print("[-] cannot reach the site...")

# response.status_code