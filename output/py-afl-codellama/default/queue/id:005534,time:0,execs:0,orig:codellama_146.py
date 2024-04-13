import sqlite3

# Open a connection to the database
conn = sqlite3.connect('demo_data.sqlite')

# Create a cursor object to execute SQL commands
cur = conn.cursor()

# Execute an INSERT statement to add a new row to the table
cur.execute("INSERT INTO demo (name, x, y) VALUES ('point1', 1, 2)")

# Execute another INSERT statement to add another new row to the table
cur.execute("INSERT INTO demo (name, x, y) VALUES ('point2', 3, 4)")

# Execute a SELECT statement to retrieve all rows from the table
results = cur.execute("SELECT * FROM demo")

# Print the results of the SELECT statement
for row in results:
    print(row[0])
    print(row[1])
    print(row[2])

# Close the cursor and connection to the database
cur.close()
conn.close()