import sqlite3

# create a connection to the database
conn = sqlite3.connect('test.db')

# create a cursor object
c = conn.cursor()

# execute a query to insert a row into the table
c.execute("INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com')")

# commit the changes
conn.commit()

# execute a query to retrieve all rows from the table
c.execute("SELECT * FROM users")

# print the results
for row in c:
    print(row)

# close the cursor and connection
c.close()
conn.close()