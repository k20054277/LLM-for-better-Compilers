
import sqlite3

# Connect to a SQLite database
conn = sqlite3.connect('test.db')

# Create a cursor object
cur = conn.cursor()

# Create a table
cur.execute("""CREATE TABLE IF NOT EXISTS employees (
    id INTEGER NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    salary INTEGER NOT NULL
)""")

# Insert data into the table
cur.execute("""INSERT INTO employees (name, salary) VALUES ('John Doe', 50000), ('Jane Doe', 60000), ('Peter Pan', 70000)""")

# Retrieve data from the table
cur.execute("""SELECT * FROM employees""")

# Print the results
for row in cur:
    print(row)

# Close the connection
conn.close()
