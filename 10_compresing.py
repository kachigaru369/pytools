import shutil
import os

loot_dir = "/tmp/.loot"
archive = "/tmp/.sysdata.zip"

if os.path.exists(loot_dir):
    shutil.make_archive("/tmp/.sysdata","zip",loot_dir)
    print(f"[+] archived created:{archive}")
else:
    print("[-] loot folder not found")

# shutil.make_archive("/tmp/.sysdata","zip",loot_dir)