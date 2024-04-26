
# Importing the sqlite3 module
import sqlite3

# Creating a connection to the database (:memory: is a built-in name for in-memory database)
connection = sqlite3.connect(':memory:')

# Creating a cursor object
cursor = connection.cursor()

# Creating a new table 'employees' with columns 'id', 'name', and 'age'
cursor.execute('''CREATE TABLE employees (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER);''')

# Inserting some records into the table using an SQL statement with placeholders
records = [('John Doe', 30), ('Jane Doe', 28), ('Bob Smith', 45)]
placeholders = ', '.join(['%s'] * len(records))
cursor.executemany('INSERT INTO employees (name, age) VALUES (%s, %s)', records)

# Retrieving data from the table using an SQL statement with a placeholder and fetchone() method
row = cursor.fetchone()
print(f'The first employee has id={row[0]}, name={row[1]}, and age={row[2]}')

# Updating a record using an SQL statement and the execute() method (using as keyword for renaming columns)
cursor.execute('UPDATE employees SET age = age + 1 WHERE name = %s', ('John Doe',))

# Renaming columns during SELECT query using the as keyword
cursor.execute('SELECT id, name AS full_name, age FROM employees ORDER BY id DESC')
rows = cursor.fetchall()
for row in rows:
    print(f'ID: {row[0]}, Full Name: {row[1]}, Age: {row[2]}')

# Closing the connection
connection.close()
