import re
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

loader:list[str]=[
    "class CustomImageLoader:",
    "    def __init__(self, map_path, use_object_storage=False):",
    "        self.map_path = map_path",
    "        self.use_object_storage = use_object_storage",
    "    def open(self):",
    "        if self.use_object_storage:",
    "            response = requests.get('http://image_storage:8082/images/' + self.map_path)",
    "            if response.status_code == 200:",
    "                image_blob = np.array(Image.open(BytesIO(response.content)))",
    "                return image_blob",
    "            else:",
    "                print(f\"Failed to fetch image {self.map_path}. Status code: {response.status_code}\")",
    "                return None",
    "        else:",
    "            # Load image locally",
    "            with Image.open(self.map_path) as image:",
    "                image_blob = np.array(image)",
    "            return image_blob"
]

def transform(filename:str="main.py"):
    with open(filename, 'r') as file:
        lines = file.readlines()

    new_lines = []
    new_lines.append("import requests\n\n")  
    for line in loader:
        new_lines.append(line)  
    new_lines.append('\n')
    for line in lines:
        if "threading.Thread" in line:
            line = line.rstrip()
            leading_spaces:int=len(line) - len(line.lstrip(' '))
            replacement_line:str=""
            for char in range(0,leading_spaces):
                replacement_line+=" "
            replacement_line+='requests.request("GET", "http://ecosystem:8081")\n'
        elif "task." in line:
            print(line+'\n\n\n')
            replacement_line="\n"
        else:
            replacement_line=line
        new_lines.append(replacement_line)

    with open(filename, 'w') as file:
        file.writelines([""])

transform()