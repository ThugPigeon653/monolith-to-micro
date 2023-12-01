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
            replacement_line+='sql_server = os.getenv(\"SQL_SERVER\")\nsql_uid = os.getenv("SQL_UID")\nsql_pwd = os.getenv("SQL_PWD")\ncls.connection = psycopg2.connect(\n    host=sql_server,\n    port=5432,\n    database=sql_uid,\n    user=sql_uid,\n    password=sql_pwd\n)\ncls.cursor = cls.connection.cursor()\n'
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