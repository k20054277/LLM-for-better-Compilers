import sqlalchemy
from sqlalchemy import create_engine

# Connect to a database using SQLAlchemy
engine = create_engine('sqlite:///path/to/database.db')

# Create a table with a column that is a Boolean type
connection = engine.connect()
connection.execute("CREATE TABLE mytable (id INTEGER PRIMARY KEY, name TEXT, active BOOLEAN)")

# Insert some data into the table
data = [
    {"name": "Alice", "active": True},
    {"name": "Bob", "active": False},
    {"name": "Charlie", "active": True}
]
connection.execute("INSERT INTO mytable (name, active) VALUES (:name, :active)", data)

# Query the table and filter based on the value of the active column
result = connection.execute("SELECT * FROM mytable WHERE active = False")
for row in result:
    print(row)