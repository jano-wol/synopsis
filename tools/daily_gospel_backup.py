import os

# Folder path
folder_path = r"C:\Repositories\synopsis\tools\data"

# Iterate through all files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    with open(file_path, 'r') as file:
        lines = file.readlines()
    found = False
    for i in range(len(lines) - 2):  # Ensure there are at least two lines ahead
        if lines[i].strip() == "________" and lines[i + 1].strip() == "" and lines[i + 2].strip() == "Gospel":
            if i + 3 < len(lines):
                below_gospel = lines[i + 3].strip()
                print(f"{filename[0:4]}-{filename[4:6]}-{filename[6:8]} : {below_gospel}")
                found = True
    if not found:
        print(f"File: {filename} : FAIL")



