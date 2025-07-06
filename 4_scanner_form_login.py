import requests
from bs4 import BeautifulSoup

url = input("enter your url:")

try:
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")
    forms = soup.find_all("form")

    print(f"\n[+] found {len(forms)} forms")
    
    for i, form in enumerate(forms):
        print(f"form #{i+1}")
        print(f"action:", form.get("action"))
        print(f"method:", form.get("method"))
        
        inputs = form.find_all("input")
        for input_tag in inputs:
            input_type = input_tag.get("type")
            input_name = input_tag.get("name")
            print(f"input: type = {input_type}, name = {input_name}")

        print("-" * 40)

except:
    print("[-] Error fetching the page or the parsing html")



# html = response.text
# BeautifulSoup(html, "html.parser")
# soup.find_all("form")
# enumerate(forms)
# form.get("action")