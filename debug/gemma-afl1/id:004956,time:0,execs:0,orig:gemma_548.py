
# Demonstrate the use of None and garbage collection

# Define a class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}, Salary: {self.salary}"

# Create an employee object
employee = Employee("John Doe", 50000)

# Print the employee object
print(employee)

# Assign None to the employee object
employee = None

# Check if the employee object is garbage collected
print(employee is None)

# Run the garbage collector
gc.collect()

# Check if the employee object has been garbage collected
print(employee is None)

# Output:
# Name: John Doe, Salary: 50000
# True
# True
