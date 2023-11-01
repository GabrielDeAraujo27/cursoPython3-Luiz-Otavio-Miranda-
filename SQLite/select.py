import sqlite3
from main import DB_FILE, TABLE_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(f'select * from {TABLE_NAME}')

for row in cursor.fetchall():
    #print(row)
    print(f'id = {row[0]}', f'nome = {row[1]}', 
          f'peso = {row[2]}', sep=(f' '*10))

cursor.close()
connection.close