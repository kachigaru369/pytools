import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_all_forms(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser").find_all("form"), response.url
    except Exception as e:
        print(f"[-] Failed to fetch forms: {e}")
        return [], url

def display_form_info(forms):
    print(f"\n[+] Found {len(forms)} forms.")
    for i, form in enumerate(forms):
        print(f"\nForm #{i+1}")
        print("  Action:", form.get("action", "[None]"))
        print("  Method:", form.get("method", "GET").upper())
        inputs = form.find_all(["input", "textarea", "select"])
        for input_tag in inputs:
            input_name = input_tag.get("name")
            if not input_name:
                continue
            input_type = input_tag.get("type", "text") if input_tag.name == "input" else input_tag.name
            print(f"    - {input_tag.name}: type = {input_type}, name = {input_name}")
        print("-" * 40)

def fill_form(form):
    data = {}
    for input_tag in form.find_all(["input", "textarea", "select"]):
        name = input_tag.get("name")
        if not name:
            continue

        input_type = input_tag.get("type", "text") if input_tag.name == "input" else input_tag.name
        default_value = input_tag.get("value", "")

        if input_type in ["hidden", "submit"]:
            data[name] = default_value
        else:
            try:
                user_input = input(f"[+] Enter value for '{name}' ({input_type}): ")
                data[name] = user_input
            except KeyboardInterrupt:
                print("\n[-] Input cancelled.")
                exit()
    return data

def send_form(form, base_url, data):
    try:
        action = form.get("action")
        full_url = urljoin(base_url, action) if action else base_url
        method = form.get("method", "get").lower()

        print(f"\n[*] Submitting to: {full_url} via {method.upper()}")
        if method == "post":
            res = requests.post(full_url, data=data)
        else:
            res = requests.get(full_url, params=data)

        print(f"[+] Response Status: {res.status_code}")
        print("[+] Response Preview:\n", res.text[:500])
    except Exception as e:
        print(f"[-] Submission failed: {e}")

# MAIN
url = input("Enter full page URL: ").strip()
forms, real_url = get_all_forms(url)

if not forms:
    print("[-] No forms found on the page.")
    exit()

display_form_info(forms)

try:
    choice = int(input(f"\n[?] Enter form number to use (1–{len(forms)}): "))
    if choice < 1 or choice > len(forms):
        print("[-] Invalid form number.")
        exit()
except ValueError:
    print("[-] Please enter a valid number.")
    exit()

selected_form = forms[choice - 1]
data = fill_form(selected_form)
send_form(selected_form, real_url, data)















# import requests
# from bs4 import BeautifulSoup

# url = input("enter your url:")

# try:
#     response = requests.get(url)
#     html = response.text

#     soup = BeautifulSoup(html, "html.parser")
#     forms = soup.find_all("form")

#     print(f"\n[+] found {len(forms)} forms")
    
#     for i, form in enumerate(forms):
#         print(f"form #{i+1}")
#         print(f"action:", form.get("action"))
#         print(f"method:", form.get("method"))
        
#         inputs = form.find_all(["input", "textarea", "select"])
#         for input_tag in inputs:
#             tag_type = input_tag.name  # input, textarea, select
#             input_type = input_tag.get("type", "text")  # textarea/select may not have type
#             input_name = input_tag.get("name")
#             print(f"{tag_type}: type = {input_type}, name = {input_name}")

#         print("-" * 40)

# except:
#     print("[-] Error fetching the page or the parsing html")



# # html = response.text
# # BeautifulSoup(html, "html.parser")
# # soup.find_all("form")
# # enumerate(forms)
# # form.get("action")