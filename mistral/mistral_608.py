
import sqlite3

# Create a new SQLite database with the given name.
def create_connection(db_file):
 db = None
 try:
     db = sqlite3.connect(db_file)
 except sqlite3.Error as e:
     print(e)
 return db

# Create a table in the SQLite database with the given name and columns.
def create_table(db, table_name, columns):
 try:
     cursor = db.cursor()
     cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({", ".join([f"{col[0]} {col[1]}" for col in columns])});')
 except sqlite3.Error as e:
     print(e)

# Insert a new row into the given table with the given key-value pairs.
def insert_into_table(db, table_name, data):
 try:
     cursor = db.cursor()
     keys, values = zip(*data.items())
     query = f'INSERT INTO {table_name} VALUES ({", ".join(["?" for _ in keys])});'
     cursor.execute(query, tuple(values))
     db.commit()
 except sqlite3.Error as e:
     print(e)

# Query the SQLite database and return all rows from the given table.
def query_table(db, table_name):
 try:
     cursor = db.cursor()
     cursor.execute(f"SELECT * FROM {table_name};")
     rows = cursor.fetchall()
     return rows
 except sqlite3.Error as e:
     print(e)
     return []

# Main function demonstrating the usage of True and sqlite3.
def main():
 db_file = "example.db"
 if not create_connection(db_file):
     return

 create_table(db_file, "my_table", [("id", "INTEGER PRIMARY KEY AUTOINCREMENT"), ("name", "TEXT")])

 data = [{"name": "Alice"}, {"name": "Bob"}]
 insert_into_table(db_file, "my_table", data)

 rows = query_table(db_file, "my_table")
 for row in rows:
     print(row)

 if True:  # Unreachable statement to demonstrate True's use.
     print("True is a boolean value representing truth.")

 create_connection(db_file).close()

if __name__ == "__main__":
 main()
