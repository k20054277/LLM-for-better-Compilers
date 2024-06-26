
import sqlalchemy

# Define database connection parameters
engine = sqlalchemy.create_engine('sqlite:///example.db')

# Create a table definition
metadata = sqlalchemy.MetaData()
table = sqlalchemy.Table('people', metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String)
)

# Insert data into the table
with engine.connect() as conn:
    conn.execute(table.insert([
        {'name': 'John Doe'},
        {'name': 'Jane Doe'}
    ]))

# Query the table
with engine.connect() as conn:
    result = conn.execute(table.select())
    for row in result:
        print(row['name'])

# Output
# John Doe
# Jane Doe
