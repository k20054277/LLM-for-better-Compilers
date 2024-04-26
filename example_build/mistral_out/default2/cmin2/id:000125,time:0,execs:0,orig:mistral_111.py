
import sqlite3

# Create a new SQLite database connection and cursor
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('example.db')
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    cursor = conn.cursor()
    table_query = """CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        is_active BOOLEAN NOT NULL);"""
    cursor.execute(table_query)

def insert_data(conn):
    cursor = conn.cursor()
    data = [(1, 'John Doe', True),
            (2, 'Jane Doe', False)]
    for row in data:
        query = """INSERT INTO users VALUES (?, ?, ?)"""
        cursor.execute(query, row)

def query_data(conn):
    cursor = conn.cursor()
    query = "SELECT id, name, is_active FROM users WHERE is_active = ?"
    False_value = False
    cursor.execute(query, (False_value,))
    rows = cursor.fetchall()

    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, is_active: {row[2]}")

if __name__ == '__main__':
    connection = create_connection()
    if connection is not None:
        create_table(connection)
        insert_data(connection)
        query_data(connection)
        connection.commit()
        connection.close()
