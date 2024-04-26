
import sqlalchemy

# Define database connection parameters
db_url = "postgresql://localhost:5432/test_db"

# Create a database engine object
engine = sqlalchemy.create_engine(db_url)

# Define SQL query
query = "SELECT * FROM employees"

# Execute the query
result = engine.execute(query)

# Print the results
for row in result:
    print(row)

# Close the database connection
engine.dispose()
