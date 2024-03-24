
import sqlite3

# Connect to a SQLite database
conn = sqlite3.connect('test.db')

# Create a cursor object
c = conn.cursor()

# Create a table
c.execute("""CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    salary INTEGER NOT NULL
)""")

# Insert data into the table
c.execute("""INSERT INTO employees (name, salary) VALUES ('John Doe', 50000), ('Jane Doe', 60000), ('Peter Pan', 70000)""")

# Retrieve data from the table
c.execute("""SELECT * FROM employees""")

# Print the results
for row in c:
    print(row)

# Commit the changes to the database
conn.commit()

# Close the connection
conn.close()
