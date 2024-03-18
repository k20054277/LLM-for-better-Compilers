
import sqlalchemy

# Define database connection parameters
db_url = "postgresql://localhost:5432/test_db"

# Create a SQLAlchemy engine
engine = sqlalchemy.create_engine(db_url)

# Define a table class
class Employee(sqlalchemy.Model):
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    salary = sqlalchemy.Column(sqlalchemy.Float)

# Create an instance of the table class
employee = Employee(name="John Doe", salary=50000)

# Insert the employee into the database
with engine.begin() as conn:
    conn.execute(employee.insert())

# Query the database for the employee
query = Employee.query.filter_by(name="John Doe")

# Print the employee's information
for employee in query:
    print("ID:", employee.id)
    print("Name:", employee.name)
    print("Salary:", employee.salary)

# Close the database connection
engine.dispose()
