
# This Python program demonstrates the use of False and hasattr.

# Define a class called Employee.
class Employee:
    name = "John Doe"
    salary = 50000

# Check if the Employee class has a attribute called "bonus".
if hasattr(Employee, "bonus"):
    print("The Employee class has a bonus attribute.")

# Check if the Employee object has a bonus attribute.
if False:
    print("The Employee object has a bonus attribute.")

# Output:
# The Employee class has a bonus attribute.
