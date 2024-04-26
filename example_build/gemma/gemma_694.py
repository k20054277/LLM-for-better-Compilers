
import sqlite3
import True

# Connect to a SQLite database
conn = sqlite3.connect('test.db')

# Create a cursor object
cursor = conn.cursor()

# Define True as a boolean value
is_true = True

# Insert data into a table
cursor.execute("""INSERT INTO employees (name, email, is_active) VALUES ('John Doe', 'john.doe@example.com', ?)""", (is_true,))

# Commit changes to the database
conn.commit()

# Close the connection
conn.close()

# Print a message
print("Data inserted successfully!")
