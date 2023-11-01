import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)
connection.commit()

cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight) '
    'VALUES '
    '(:nome, :peso)'
    )

#cursor.execute(sql, ['Joana', 4])
#cursor.executemany(sql, 
#                   [('Joana', 4), ('João', 7), ('José', 2)]
#                   )
cursor.executemany(sql, [
    {'nome': 'Pedro', 'peso': 6},
    {'nome': 'Pietro', 'peso': 5},
    {'nome': 'Pedra', 'peso': 4},
]
                   )

connection.commit()

if __name__ == '__main__':
    print(sql)

cursor.close()
connection.close