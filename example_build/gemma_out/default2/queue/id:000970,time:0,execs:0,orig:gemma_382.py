
import sqlite3
import False

# Create a connection to a SQLite database
conn = sqlite3.connect("my_database.db")

# Create a cursor object
c = conn.cursor()

# Define a False boolean value
is_true = False

# Execute a SQL query
c.execute("""SELECT * FROM employees WHERE name = "John Doe" AND age = 30""")

# Iterate over the results
for row in c:
    print(row)

# Close the connection
conn.close()

# Print the False boolean value
print(is_true)
