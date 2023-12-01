import re
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

loader:list[str]=[
    "class CustomImageLoader:\n",
    "    def __init__(self, map_path, use_object_storage=False):\n",
    "        self.map_path = map_path\n",
    "        self.use_object_storage = use_object_storage\n",
    "    def open(self):\n",
    "        if self.use_object_storage:\n",
    "            response = requests.get('http://image_storage:8082/images/' + self.map_path)\n",
    "            if response.status_code == 200:\n",
    "                image_blob = np.array(Image.open(BytesIO(response.content)))\n",
    "                return image_blob\n",
    "            else:\n",
    "                print(f\"Failed to fetch image {self.map_path}. Status code: {response.status_code}\")\n",
    "                return None\n",
    "        else:\n",
    "            # Load image locally\n",
    "            with Image.open(self.map_path) as image:\n",
    "                image_blob = np.array(image)\n",
    "            return image_blob\n"
]

def transform(filename:str="main.py"):
    with open(filename, 'r') as file:
        lines = file.readlines()

    new_lines = []
    new_lines.append("import requests\n\n")  
    new_lines.append("from io import BytesIO\n\n")  
    new_lines.append("import numpy as np\n\n")  
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
        elif "task." in line or "world_visualizer" in line:
            replacement_line="\n"
        else:
            replacement_line=line
        new_lines.append(replacement_line)

    with open(filename, 'w') as file:
        file.writelines(new_lines)

transform()