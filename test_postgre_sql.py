import sqlite3
import pandas as pd

def setup_in_memory_db():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
    ''')
    cursor.executemany('''
    INSERT INTO users (name, age) VALUES (?, ?)
    ''', [('Sahil', 22), ('sa', 35), ('hi', 45), ('ls', 28)])
    conn.commit()
    return conn

def query_db(conn, query):
    df = pd.read_sql_query(query, conn)
    return df

conn = setup_in_memory_db()
query = 'SELECT * FROM users WHERE name = "Sahil";'
result = query_db(conn, query)
print(result)

conn.close()
