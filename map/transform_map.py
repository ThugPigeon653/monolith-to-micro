import os
import requests

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

def transform(filename:str="map.py"):
    with open(filename, 'r') as file:
        lines = file.readlines()

    new_lines = []
    new_lines.append("import requests\n")
    new_lines.append("from io import BytesIO\n") 
    new_lines.append('\n')
    new_lines.append('def get_conn():\n')
    new_lines.append('  sql_server = os.getenv(\"SQL_SERVER\")\n')
    new_lines.append('  sql_uid = os.getenv("SQL_UID")\n')
    new_lines.append('  sql_pwd = os.getenv("SQL_PWD")\n')
    new_lines.append('  connection = psycopg2.connect(\n')
    new_lines.append('      host=sql_server,\n')
    new_lines.append('      port=5432,\n')
    new_lines.append('      database=sql_uid,\n')
    new_lines.append('      user=sql_uid,\n')
    new_lines.append('      password=sql_pwd\n')
    new_lines.append('  )\n')
    new_lines.append('  return connection\n')
    new_lines.append('\n')
    for subline in loader:
        new_lines.append(subline)
    new_lines.append('\n')
    for line in lines:
        replacement_line:str=""
        is_written_connection:bool=False
        if not is_written_connection and line.strip()=="":
            is_written_connection=True
        if ("animal_database.db" in line and "sqlite3.connect" not in line) or "db_connection" in line:
            replacement_line="\n"
        elif "sqlite3.connect" in line:
            replacement_line=line.split('=')[0]+'=get_conn()\n'
        elif "import sqlite3" in line:
            replacement_line="import psycopg2\n"
        else:
            replacement_line=line
        replacement_line.replace("Image", "CustomImageLoader")
        new_lines.append(replacement_line)

    with open(filename, 'w') as file:
        file.writelines(new_lines)

transform()
