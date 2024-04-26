
# This Python program demonstrates the use of True and hasattr functions

# Define a class named Employee
class Employee:
    name = "John Doe"
    salary = 50000

# Check if the Employee class has a member named name
if hasattr(Employee, "name"):
    print("The Employee class has a member named name.")

# Check if the Employee class has a member named salary
if hasattr(Employee, "salary"):
    print("The Employee class has a member named salary.")

# Check if the Employee object has a member named name
if True and hasattr(Employee(), "name"):
    print("The Employee object has a member named name.")

# Check if the Employee object has a member named salary
if True and hasattr(Employee(), "salary"):
    print("The Employee object has a member named salary.")

# Output:
# The Employee class has a member named name.
# The Employee class has a member named salary.
# The Employee object has a member named name.
# The Employee object has a member named salary.
