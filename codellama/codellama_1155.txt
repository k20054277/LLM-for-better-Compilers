import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create a table called "users" with columns "id", "name", and "age"
c.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")

# Insert some rows into the table
c.execute("INSERT INTO users VALUES (1, 'Alice', 30)")
c.execute("INSERT INTO users VALUES (2, 'Bob', 35)")
c.execute("INSERT INTO users VALUES (3, 'Charlie', 40)")

# Select all rows from the table where "age" is greater than 30
c.execute("SELECT * FROM users WHERE age > 30")
print(c.fetchall())

# Close the connection to the database
conn.close()