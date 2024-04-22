import sqlite3

conn = sqlite3.connect('users.db')
c = conn.cursor()

# Create a new table called 'users'
c.execute('''CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)''')

# Insert some sample data into the table
c.execute("INSERT INTO users VALUES(1, 'John Doe', 'johndoe@example.com')")
c.execute("INSERT INTO users VALUES(2, 'Jane Doe', 'janedoe@example.com')")
c.execute("INSERT INTO users VALUES(3, 'Bob Smith', 'bobsmith@example.com')")

# Query the data from the table
c.execute('SELECT * FROM users')
rows = c.fetchall()
print(rows)

# Update a row in the table
c.execute("UPDATE users SET name='Jane Doe' WHERE id=2")
conn.commit()

# Delete a row from the table
c.execute("DELETE FROM users WHERE id=3")
conn.commit()

conn.close()