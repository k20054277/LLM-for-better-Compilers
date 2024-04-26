
import sqlite3

# Connect to a SQLite database
conn = sqlite3.connect('my_database.db')

# Create a cursor object
cursor = conn.cursor()

# Create a SQL query
query = "SELECT * FROM employees"

# Execute the query
cursor.execute(query)

# Fetch all results
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
