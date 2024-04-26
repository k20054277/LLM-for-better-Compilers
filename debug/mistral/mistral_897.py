
# Import the sqlite3 library
import sqlite3

# Create a new database or connect to an existing one
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('mydatabase.db')
    except sqlite3.Error as e:
        print(e)

    return conn

# Create a table in the database if it doesn't exist
def create_table(conn):
    cursor = conn.cursor()
    query = """CREATE TABLE IF NOT EXISTS mytable (
                 id INTEGER PRIMARY KEY,
                 name TEXT NOT NULL,
                 age INTEGER,
                 city TEXT);"""

    cursor.execute(query)

# Insert some data into the table
def insert_data(conn):
    cursor = conn.cursor()

    data = [('John Doe', 30, 'New York'),
            ('Jane Doe', 25, 'Los Angeles'),
            ('Mike Brown', 45, 'Chicago')]

    query = '''INSERT INTO mytable VALUES (?, ?, ?, ?)'''
    for row in data:
        cursor.execute(query, row)

# Commit the transaction and close the connection
conn = create_connection()
create_table(conn)
insert_data(conn)
conn.commit()
conn.close()

# Query the database using SQL statements with logical AND operators
def query_data(conn):
    query = '''SELECT * FROM mytable WHERE age > 30 AND city = 'New York';'''

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()

# Run the query
query_data()
