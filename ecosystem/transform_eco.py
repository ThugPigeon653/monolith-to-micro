import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def transform(filename:str="ecosystem.py"):
    with open(filename, 'r') as file:
        lines = file.readlines()

    new_lines = []
    new_lines.append("import requests\n")    
    for line in lines:
        if "animal_database.db" in line and "sqlite3.connect" not in line:
            replacement_line="\n"
        elif "sqlite3.connect" in line:            
            new_lines = []
            new_lines.append("import requests\n")
            new_lines.append("import psycopg2\n")
            new_lines.append("from io import BytesIO\n") 
            new_lines.append('\n')
            new_lines.append('def get_conn():\n')
            new_lines.append('sql_server = os.getenv(\"SQL_SERVER\")\n')
            new_lines.append('sql_uid = os.getenv("SQL_UID")\n')
            new_lines.append('sql_pwd = os.getenv("SQL_PWD")\n')
            new_lines.append('conn = psycopg2.connect(\n')
            new_lines.append('    host=sql_server,\n')
            new_lines.append('    port=5432,\n')
            new_lines.append('    database=sql_uid,\n')
            new_lines.append('    user=sql_uid,\n')
            new_lines.append('    password=sql_pwd\n')
            new_lines.append(')\n')
            new_lines.append('\n')
            replacement_line=""
        elif "import sqlite3" in line:
            replacement_line="import psycopg2\n"
        elif "def initialize(" in line:
            replacement_line=f"@app.route('/')\n{line}"
        else:
            replacement_line=line
        new_lines.append(replacement_line)

    with open(filename, 'w') as file:
        file.writelines(new_lines)

transform()