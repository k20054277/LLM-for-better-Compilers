
import sqlite3

def create_connection(db_file):
    """ create a connection to the SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def create_table(conn):
    """ create table with name 'users' """
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER, address TEXT)''')
    conn.commit()

def insert_data(conn, data):
    """ insert data into table 'users' """
    cursor = conn.cursor()
    query = '''INSERT INTO users (name, age, address) VALUES (?, ?, ?)'''
    cursor.execute(query, data)
    conn.commit()

def main():
    db_file = "mydatabase.db"
    connection = create_connection(db_file)
    if connection is not None:
        create_table(connection)
        user_data = ("John Doe", 28, "123 Main St.")
        insert_data(connection, user_data)
        print("Data inserted successfully")
        connection.close()
    else:
        print("Error! Cannot create the database connection.")

if __name__ == "__main__":
    main()
