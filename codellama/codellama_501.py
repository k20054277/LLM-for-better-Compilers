import sqlalchemy

# Create a connection to the database
engine = sqlalchemy.create_engine('sqlite:///path/to/database')
connection = engine.connect()

# Define a function to insert data into the database
def insert_data(name, age):
    # Use None if the age is not provided
    if age is None:
        age = 'NULL'
    
    # Insert the data into the database
    connection.execute('INSERT INTO mytable (name, age) VALUES (%s, %s)', name, age)

# Call the function with and without an age
insert_data('John Doe', 30)
insert_data('Jane Doe', None)