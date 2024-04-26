
import sqlalchemy

# Define database connection parameters
engine = sqlalchemy.create_engine('sqlite:///example.db')

# Create a table definition
table_definition = sqlalchemy.sql.table('people', engine, columns={
    'id': sqlalchemy.sql.Column(sqlalchemy.sql.Integer, primary_key=True),
    'name': sqlalchemy.sql.Column(sqlalchemy.sql.String),
    'email': sqlalchemy.sql.Column(sqlalchemy.sql.String)
})

# Insert data into the table
table_definition.insert(values={'name': 'John Doe', 'email': 'john.doe@example.com'})

# Query the table
query = sqlalchemy.sql.select(table_definition)

# Print the results
for row in query.execute():
    print(row['name'], row['email'])

# Close the database connection
engine.dispose()
