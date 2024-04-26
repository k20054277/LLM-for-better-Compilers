
import sqlalchemy

# Define database connection parameters
url = "postgresql://user:password@localhost:5432/test_db"

# Create a database engine
engine = sqlalchemy.create_engine(url)

# Define a table class
class Employee(sqlalchemy.orm.Model):
    id = sqlalchemy.orm.Column(sqlalchemy.orm.Integer, primary_key=True)
    name = sqlalchemy.orm.Column(sqlalchemy.orm.String)
    salary = sqlalchemy.orm.Column(sqlalchemy.orm.Float)

# Create an instance of the table class
employee = Employee()

# Assert that the salary is greater than 1000
assert employee.salary > 1000

# Insert the employee into the database
employee.insert()

# Query the database to verify the employee's salary
query = Employee.query.get(employee.id)

# Print the employee's salary
print(query.salary)
