
import sqlalchemy

# Define database connection parameters
db_url = "postgresql://user:password@localhost:5432/test_database"

# Create a SQLAlchemy engine
engine = sqlalchemy.create_engine(db_url)

# Define a query using SQLAlchemy
query = sqlalchemy.orm.query(sqlalchemy.orm.relationship('Model'))

# Execute the query
results = query.all()

# Print the results
for result in results:
    print(result.name)

# Close the database connection
engine.dispose()
