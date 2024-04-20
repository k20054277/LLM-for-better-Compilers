from sqlalchemy import create_engine, MetaData, Table, Column, Integer

# Create a database engine object
engine = create_engine('sqlite:///example.db')

# Define the table and columns
metadata = MetaData()
table = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('age', Integer)
)

# Create the database if it doesn't exist
if not engine.dialect.has_table(engine, table.name):
    metadata.create_all(engine)

# Insert some data into the table
with engine.begin() as connection:
    connection.execute(table.insert(), [
        {'id': 1, 'name': 'Alice', 'age': 25},
        {'id': 2, 'name': 'Bob', 'age': 30},
        {'id': 3, 'name': 'Charlie', 'age': 35}
    ])

# Query the data from the table
with engine.begin() as connection:
    result = connection.execute(table.select())
    for row in result:
        print(row)

# Delete a row from the table
with engine.begin() as connection:
    connection.execute(table.delete().where(table.c.id == 2))