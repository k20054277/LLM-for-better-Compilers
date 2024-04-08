import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table

# Create a connection engine to the database
engine = create_engine('postgresql://user:password@host:port/database')

# Define the metadata of the table
metadata = MetaData()
table = Table('mytable', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('age', Integer)
)

# Create the table in the database
metadata.create_all(engine)

# Insert some data into the table
data = [
    {'id': 1, 'name': 'Alice', 'age': 25},
    {'id': 2, 'name': 'Bob', 'age': 30},
    {'id': 3, 'name': 'Charlie', 'age': 35}
]
table.insert().values(data).execute()

# Query the table and print the results
result = table.select().where(table.c.age > 30).order_by(table.c.id)
for row in result:
    print(row.name, row.age)